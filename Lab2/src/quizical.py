#!/usr/bin/python
# =============================================================================
#        File : Quizical.py
# Description : Quiz Server for Quiz Devices
#      Author : Drew Gislsason
#        Date : 3/8/2017
# =============================================================================
"""
  Quizical is a simple Quiz server suitable for classrooms.

  See quizical.md for the API description

  TODO: base64 pwd
  TODO: Allow throwing bad values at framework
  TODO: Add multiple instructors
  TODO: Add multiple quizzes
  TODO: Allow students to take quiz at their own pace
  TODO: Allow quizes to expire (e.g. allow a quiz to expire after 24 hours)
  TODO: Database of quizes
  TODO: Provide hooks into grading systems such as Canvas

  Places to host: Heroku, OpenShift, AWS
"""
import random
import string
import base64
import json
import sys

PORT = 5000

from flask import Flask, request

# ============================== Data ====================================

# create the global objects
app = Flask(__name__)

DEBUG = 1
UNIT_TEST = 0

# HTTP response codes used by this application
STATUS_OK         = 200
STATUS_CREATED    = 201
STATUS_NO_CONTENT = 204
STATUS_BAD_REQUEST= 400
STATUS_FORBIDDEN  = 403

# bit map of access rights
ACCESS_STUDENT    = 0
ACCESS_TEACHER    = 1

curquiz = {"name":"osi7layer", "question":"1", "answer":"A"}

quizzes = {
  "python": {
    "questions": {
      "1" : [ "How do you create a variable with the value 5 in Python?",
        " A. var x = 5",
        " B. def x = 5",
        "*C. x = 5",
        " D. import 5" ],
      "2": [ "How do you create a function in Python?",
        "*A. def my_func(param=None):",
        " B. int my_func(var param):",
        " C. proc my_func(int param):",
        " D. my_func(param=5)" ],
      "3": [ "How do you create a for loop from 1 to 10 in Python?",
        " A: for(i = 1 to 10)",
        " B: for i = 1 to 10 do",
        " C: for i in xrange(1,10):",
        "*D: for i in xrange(1,11):" ],
      "4": [ "How do you create an if statement with three conditionals in Python?",
        "*A: if a and b and c:",
        " B: if a && b && c:",
        " C: if(a && b && c) {",
        " D: This can't be done in Python" ],
      "5": [
        "How do you make a Python file executable directly in the terminal?",
        " A: Add line '#!/usr/bin/python' at start of file",
        " B: Python files are always executable",
        " C: Create a .pyc file",
        "*D: Add line '#!/usr/bin/python' at start of file and chmod +X file" ]
    }
  },
  "osi7layer": {
    "questions": {
      "1" : [ "What best describes the PHY layer?",
        "*A. It is the physical modulation layer (e.g. wireless or wired)",
        " B. It is for medical (physician) devices",
        " C. It is for signal quality (fidelity)",
        " D. It is the study of plants (phytology)" ],
      "2": [ "What best describes DATA LINK or MAC layer?",
        " A. For end-to-end routing",
        " B. Link quality",
        "*C. Allows multiple devices to share the PHY",
        " D. Not part of the OSI model" ],
      "3": [ "What best describes the Network Layer?",
        " A: Defines application protocol",
        " B: For quality of service",
        " C: Publish/subscribe",
        "*D: For end-to-end routing" ],
      "4": [ "Name all 7 layers in order from lowest to highest",
        " A: PHY, MAC, NWK, TRANSPORT, PUBLISH, BODY, APPLICATION",
        " B: PHY, DATA LINK, NETWORK, TRANSPORT, PRESENTATION, SESSION, APPLICATION",
        "*C: PHY, DATA LINK, NETWORK, TRANSPORT, SESSION, PRESENTATION, APPLICATION",
        " D: None of the above" ]
    }
  }
}

users = {
  # instructor and related
  "drewg":     { "pwd":"gislason",    "access":ACCESS_TEACHER, "token":"OyTtoKdTUweqAUuZZgwN", "answers":{}, "results":"-" },
  "joshw":     { "pwd":"welschmeyer", "access":ACCESS_STUDENT, "token":"qvsz9Q4zt2QLktbGEsVa", "answers":{}, "results":"-" },
  "steved":    { "pwd":"dame",        "access":ACCESS_STUDENT, "token":"oKfvFpsTPqwvEJ35dMwP", "answers":{}, "results":"-" },
  "richardo":  { "pwd":"ortega",      "access":ACCESS_STUDENT, "token":"jZojSwac6iNw1jlnz2Mw", "answers":{}, "results":"-" },
  "me":        { "pwd":"pass",        "access":ACCESS_STUDENT, "token":"NsAeWOvWOQ3bYlCyzmSK", "answers":{}, "results":"-" },
  "bryanp":    { "pwd":"palmer",      "access":ACCESS_STUDENT, "token":"EcQuXxkBMpxtk6qZqvMf", "answers":{}, "results":"-" },

  # students
  "jonathana": { "pwd":"andress",     "access":ACCESS_STUDENT, "token":"48OwTWLHs4cyf2IsXfET", "answers":{}, "results":"-" },
  "tamera":    { "pwd":"awad",        "access":ACCESS_STUDENT, "token":"cQyB2QHwi5tnAMzfpZos", "answers":{}, "results":"-" },
  "garethb":   { "pwd":"beale",       "access":ACCESS_STUDENT, "token":"sE5z2sqUuZsL5Y3Taww8", "answers":{}, "results":"-" },
  "danb":      { "pwd":"bittner",     "access":ACCESS_STUDENT, "token":"t7QBejIFnWGyvaczopyH", "answers":{}, "results":"-" },
  "michaelb":  { "pwd":"burgess",     "access":ACCESS_STUDENT, "token":"MQ0Q6uGNY9pO9gEbJGvc", "answers":{}, "results":"-" },
  "markb":     { "pwd":"byers",       "access":ACCESS_STUDENT, "token":"kFpTcWDPt7hFeckwkU5Q", "answers":{}, "results":"-" },
  "isaacc":    { "pwd":"chang",       "access":ACCESS_STUDENT, "token":"o45EpLs4rRxwqwJinfHr", "answers":{}, "results":"-" },
  "victorc":   { "pwd":"chinn",       "access":ACCESS_STUDENT, "token":"WdmnqqtdwIj8xl8ZmjVb", "answers":{}, "results":"-" },
  "gauravg":   { "pwd":"garg",        "access":ACCESS_STUDENT, "token":"HiQAPOBR9y2DRiBCIV6O", "answers":{}, "results":"-" },
  "thomash":   { "pwd":"harvey",      "access":ACCESS_STUDENT, "token":"yM9jMqGOn3RWiGSZEuHl", "answers":{}, "results":"-" },
  "richardh":  { "pwd":"hill",        "access":ACCESS_STUDENT, "token":"ej7JUySPElApFcaHnE5k", "answers":{}, "results":"-" },
  "machaelm":  { "pwd":"messmer",     "access":ACCESS_STUDENT, "token":"LWEYdqf15XU5eRxParDh", "answers":{}, "results":"-" },
  "dylanm":    { "pwd":"miller",      "access":ACCESS_STUDENT, "token":"fWrI0KPrfPCOhz4ETVWM", "answers":{}, "results":"-" },
  "michaelp":  { "pwd":"panciroli",   "access":ACCESS_STUDENT, "token":"nptQyw6fI2DVVDrML7BR", "answers":{}, "results":"-" },
  "thomasr":   { "pwd":"roome",       "access":ACCESS_STUDENT, "token":"4rqrLc1Z0HJ2Zl7YxBcW", "answers":{}, "results":"-" },
  "jonathans": { "pwd":"schooler",    "access":ACCESS_STUDENT, "token":"TSBXW29O8wpyA3ChPSx3", "answers":{}, "results":"-" },
  "santhoshs": { "pwd":"shetty",      "access":ACCESS_STUDENT, "token":"nkF2OXf7UrYw81asY8xP", "answers":{}, "results":"-" },
  "manis":     { "pwd":"subramanian", "access":ACCESS_STUDENT, "token":"vtV8Yphu8fMz5DwiKwLG", "answers":{}, "results":"-" },
  "joelw":     { "pwd":"ware",        "access":ACCESS_STUDENT, "token":"OWCI5EAkCugn1N0xZ4ZY", "answers":{}, "results":"-" },
  "dennisw":   { "pwd":"whetten",     "access":ACCESS_STUDENT, "token":"euCULfHcpsONhZdSnGl6", "answers":{}, "results":"-" }
}

# ============================ Helper Functions =================================

# -------------------------------

def QuizNewToken(N=20):
  """
    QuizNewToken(N=20)
    Returns random token with characters and numbers up to N chars
  """
  return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase
    + string.digits) for _ in range(N))

# -------------------------------

# helper function, returns username or None
def QuizLookupUserByToken(token):
  if token == None:
    return None
  token = str(token)
  for username in users:
    if users[username]["token"] == token:
      return username
  return None

# -------------------------------

# helper function, returns current quizname, quizques (#), and question array
def QuizLookupQuestion():
  quizname = curquiz["name"]
  quizques = curquiz["question"]
  if (quizname in quizzes) and (quizques in quizzes[quizname]["questions"]):
    question = quizzes[quizname]["questions"][quizques]
    return quizname, quizques, question
  return None, None, None

# -------------------------------

# helper function, returns username of teacher if found, or None
def QuizTeacherAccess(token):
  username = QuizLookupUserByToken(token)
  if username and users[username]["access"] == ACCESS_TEACHER:
    return username
  return None

# -------------------------------

def QuizResetTest():
  global users
  for username in users:
    users[username]["results"] = "-"
    users[username]["answers"] = {}

def QuizResetTokens():
  global users
  for user in users:
    users[user]["token"] = QuizNewToken()


# ============================ Main Code Logic =================================

# ------------------------ QuizLogin ------------------------

def QuizLogin(username,pwd):
  """
  QuizPutLogin(username,pwd)
  Returns None or a JSON string {"token":"xxxx"}
  """
  global users
  if DEBUG:
    print "QuizLogin(username=" + str(username) + ",pwd=" + str(pwd) + ")"

  # verify we know the user and trust them
  if not username in users:
    if DEBUG:
      print "  failed name"
    return None
  if pwd != users[username]["pwd"]:
    if DEBUG:
      print "  failed password"
    return None

  # get user token
  if users[username]["token"] == "-":
    users[username]["token"] = QuizNewToken()
  s = '{"token":"' + users[username]["token"] + '"}\n'
  if DEBUG:
    print s
  return s


# ------------------------ QuizProfile ------------------------

def QuizProfile(username,newpwd):
  """
  QuizPutProfile(username,newpwd)
  Returns None or a JSON string {"token":"xxxx"}
  """
  global users

  if DEBUG:
    print "QuizPutProfile(username=" + str(username) + ",newpwd=" + str(newpwd) + ")"
  if not username in users:
    return None

  users[username]["pwd"] = newpwd
  users[username]["token"] = QuizNewToken()
  s = '{"token":"' + users[username]["token"] + '"}\n'
  if DEBUG:
    print s
  return s

# ------------------------ QuizStudentQuestion ------------------------

def QuizStudentQuestion():
  """
  QuizStudentQuestion()
  Returns None or a JSON string {"quizname":{"1":[ "ques"," a1","*a2"," a3"," a4" ]}}
  """

  quizname, quizques, question = QuizLookupQuestion()
  if quizname:

    # get the quizname and question in JSON form
    rsp = '{"' + quizname + '":{"' + quizques + '":' + json.dumps(question) + '}}\n'

    # don't let student know the correct answer (starred)
    i = rsp.find('*')
    if i >= 0:
      rsp = rsp[0:i] + ' ' + rsp[i+1:]

  else:
    rsp = None

  return rsp

# ------------------------ QuizStudentAnswerGet ------------------------

def QuizStudentAnswerGet(username):
  """
  QuizStudentAnswerGet(username)
  Returns None or
          '{"correct":true,"results":"1/4","answers":{"1":"B","2":"D"}}'
  """

  # not in a quiz
  if not curquiz["name"] in quizzes:
    return None

  # determine if their answer to the current question is correct
  correct = False
  question = curquiz["question"]
  if question in users[username]["answers"] and \
    users[username]["answers"][question] == curquiz["answer"]:
    correct = True

  s = '{"correct":'
  if correct:
    s = s + 'true'
  else:
    s = s + 'false'
  s = s + ',"results":"' + users[username]["results"] + '","answers":' + \
    json.dumps(users[username]["answers"]) + '}\n'

  # return the JSON string
  return s

# ------------------------ QuizStudentAnswerPut ------------------------

def QuizStudentAnswerPut(username,answer_obj):
  """
  QuizStudentAnswerGet(username)
  Returns None or
          '{"correct":true,"results":"1/4","answers":{"1":"B","2":"D"}}'
  """

  # not in a quiz
  if not curquiz["name"] in quizzes:
    return None

  # get 1st answer out of the object
  for userques in answer_obj:
    break
  answer = answer_obj[userques]

  if DEBUG:
    print str(userques) + ":" + str(answer)

  # make sure user is answering the right question
  question = curquiz["question"]
  if userques != question:
    return None

  # don't allow answer twice
  if userques in users[username]["answers"]:
    return None

  # add into answers
  users[username]["answers"][question] = answer

  # determine if their answer to the current question is correct
  correct = False
  if curquiz["answer"] == answer:
    correct = True

  # add into results
  num_questions = len(quizzes[curquiz["name"]]["questions"])
  if users[username]["results"] == "-":
    if correct: num_correct = 1
    else:       num_correct = 0
  else:
    num_correct = int(users[username]["results"][0])
    if correct: num_correct += 1
  users[username]["results"] = str(num_correct) + "/" + str(num_questions)

  # return True since it worked, and the return JSON string
  return QuizStudentAnswerGet(username)


# ------------------------ QuizTeacherQuizGet ------------------------

# get the current quiz
def QuizTeacherQuizGet():
  if not curquiz["name"] in quizzes:
    return None
  s = '{"' + curquiz["name"] + '":' + json.dumps(quizzes[curquiz["name"]]) + '}\n'
  return s

# ------------------------ QuizTeacherQuizPut ------------------------

# put the current quiz
def QuizTeacherQuizPut(current):
  global curquiz
  if "name" in current:
    curquiz["name"] = current["name"]
  if "question" in current:
    curquiz["question"] = current["question"]
  if "answer" in current:
    curquiz["answer"] = current["answer"]

  if "reset" in curquiz:
    QuizResetTest()

  return json.dumps(curquiz)

# ------------------------ QuizTeacherResults ------------------------
def QuizTeacherResults(anon):
  s = '{'
  first = True
  for username in users:
    if first:
      first = False
    else:
      s = s + ','
    s = s + '"'
    if anon:
      s = s + QuizNewToken(6)
    else:
      s = s + username
    s = s + '":{"results":"' + users[username]["results"] + \
        '","answers":' + json.dumps(users[username]["answers"]) + '}'
  s = s + '}\n'
  return s

# =========================== API Routes =================================


# ------------------------ /debug ------------------------

@app.route("/debug", methods=['GET','POST'])
def QuizDebug():
  print "Debugging!\n"
  print "request.get_json:",
  print request.get_json(force=True,silent=True)
  print "request.get_data:",
  print request.get_data()
  print "request.args:",
  print request.args
  token = request.args.get('token')
  print "token: " + str(token)
  nothere = request.args.get('nothere')
  print "nothere: " + str(nothere)

  return json.dumps(curquiz), STATUS_OK

# ------------------------ /api/v1/login/{username} ------------------------

# allow user to log in
@app.route('/api/v1/login/<username>', methods=['GET'])
def QuizApiLogin(username):

  pwd       = request.args.get('pwd')

  if DEBUG:
    print "QuizApiLogin(username=" + username + ",pwd=" + pwd + ")"

  rsp = QuizLogin(username,pwd)
  if not rsp:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST
  return rsp, STATUS_OK


# ------------------------ /api/v1/profile ------------------------

# allow user to change password
@app.route('/api/v1/profile', methods=['PUT'])
def QuizApiProfile():
  if DEBUG:
    print "QuizApiProfile():"

  username = QuizLookupUserByToken(request.args.get('token'))
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  data = request.get_json(force=True,silent=True)
  if not "newpwd" in data:
    return 'bad request', STATUS_BAD_REQUEST
  else:
    newpwd = data["newpwd"]

  rsp = QuizProfile(username, newpwd)
  return rsp, STATUS_OK

# ------------------------ /api/v1/student/question ------------------------

# get the current question
@app.route('/api/v1/student/question', methods=['GET'])
def QuizApiStudentQuestion():

  if DEBUG:
    print "QuizApiStudentQuestion():"

  username = QuizLookupUserByToken(request.args.get('token'))
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  rsp = QuizStudentQuestion()
  if rsp == None:
    return STATUS_NO_CONTENT
  return rsp,STATUS_OK

# ------------------------ /api/v1/student/answer ------------------------

# get the current answer, or put an answer
@app.route('/api/v1/student/answer', methods=['GET', 'PUT'])
def QuizApiStudentAnswer():

  if DEBUG:
    print "QuizApiStudentAnswer():"

  username = QuizLookupUserByToken(request.args.get('token'))
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  # GET
  rsp_data = None
  if request.method == 'GET':
    rsp_data = QuizStudentAnswerGet(username)

  # PUT
  elif request.method == 'PUT':
    rsp_data = QuizStudentAnswerPut(username, request.get_json(force=True,silent=True))

  if rsp_data == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST
  return rsp_data, STATUS_OK

# ------------------------ /api/v1/teacher/quiz ------------------------

@app.route("/api/v1/teacher/quiz", methods=['GET', 'PUT', 'POST', 'DELETE' ])
def QuizApiTeacherQuiz():

  if DEBUG:
    print "QuizApiTeacherQuiz():"

  # verify teacher has access
  username = QuizTeacherAccess(request.args.get('token'))
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  if request.method == 'GET':
    rsp_data = QuizTeacherQuizGet()

  elif request.method == 'PUT':
    current = request.get_json(force=True,silent=True)
    rsp_data = QuizTeacherQuizPut(current)

  # TODO: post new quiz
  elif request.method == 'POST':
    return '',405

  # TODO: delete quiz
  elif request.method == 'DELETE':
    return '',405

  return rsp_data, STATUS_OK

# ------------------------ /api/v1/teacher/results ------------------------

@app.route("/api/v1/teacher/results", methods=['GET'])
def QuizApiTeacherResults():

  if DEBUG:
    print "QuizApiTeacherResults():"

  # get items from command line
  token = str(request.args.get('token'))
  anon  = str(request.args.get('a'))
  if str(anon) == "1":
    anon = True
  else:
    anon = False

  # verify teacher has access
  username = QuizTeacherAccess(token)
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  rsp_data = QuizTeacherResults(anon)

  return rsp_data, STATUS_OK

# ------------------------ /api/v1/teacher/admin ------------------------

@app.route("/api/v1/teacher/admin", methods=['GET', 'POST' ])
def QuizApiTeacherAdmin():
  global users

  if DEBUG:
    print "QuizTeacherAdmin():"

  # verify teacher has access
  username = QuizTeacherAccess(request.args.get('token'))
  if username == None:
    return 'BAD REQUEST\n', STATUS_BAD_REQUEST

  if request.method == 'GET':
      rsp_data = json.dumps(users) + '\n'

  elif request.method == 'POST':
    newusers = request.get_json(force=True,silent=True)
    if newusers:
      users = newusers

  return rsp_data, STATUS_OK


# ============================ Startup =================================
def QuizStartup():
  QuizResetTokens()


# ============================== Main ====================================

if __name__ == "__main__":

  # signon
  print "\nWelcome to Quizical, the simple quiz tool for teachers and students\n\n"

  QuizStartup()
  if not UNIT_TEST:
    app.debug = True
    app.run(host='0.0.0.0', port=PORT)
