#!/usr/bin/python
# =============================================================================
#        File : quiz.py
# Description : Take a Quizical Quiz
#      Author : Drew Gislsason
#        Date : 3/8/2017
# =============================================================================
import httplib
import json
import sys

# ============================== Data =========================================
QUIZ_URL  = "172.22.194.176:5000"

DEBUG     = 0

# ============================== Code ========================================

# Returns a token if worked
def QuizLogin():
  username = raw_input("Enter Username (e.g. me): ")
  pwd      = raw_input("Enter Password (e.g. pass): ")

  fullpath = '/api/v1/login/' + username + "?pwd=" + pwd
  conn = httplib.HTTPConnection(QUIZ_URL)
  conn.request('GET', fullpath )
  r1 = conn.getresponse()

  if r1.status == 200:
    data = r1.read()
    if DEBUG:
      print "data: " + data

    obj = json.loads(data)

    if DEBUG:
      print obj
    if "token" in obj:
      return obj["token"]

  return None
  conn.close()

# Returns current question, or None if no more questions
def QuizGetQuestion(token):

  fullpath = '/api/v1/student/question?token=' + token
  conn = httplib.HTTPConnection(QUIZ_URL)
  conn.request('GET', fullpath )
  r1 = conn.getresponse()

  if r1.status == 200:
    data = r1.read()
    question = json.loads(data)
    return question

  return None
  conn.close()

# Put the answer to the data base, returns 
def QuizPutAnswer(token, ques_num, answer):

  fullpath = '/api/v1/student/answer?token=' + token
  json_ans = '{"' + ques_num + '":"' + answer + '"}'

  conn = httplib.HTTPConnection(QUIZ_URL)
  conn.request('PUT', fullpath, json_ans )
  r1 = conn.getresponse()

  if r1.status == 200:
    data = r1.read()
    return data

  return None
  conn.close()

# ============================== Main ====================================
if __name__ == "__main__":

  token = QuizLogin()
  if token == None:
    print "Failed to log in"
    exit()
  else:
    print "token=" + str(token) + "\n"

  while True:
    question = QuizGetQuestion(token)
    if question == None:
      print "Failed to get question"
      exit()
    else:
      for quizname in question:
        print "Quiz: " + quizname, 
        for ques_num in question[quizname]:
          print "question: " + ques_num
          for line in question[quizname][ques_num]:
            print line
      answer = raw_input("Your answer (e.g. B): ")
      print "\n"
      results = QuizPutAnswer(token, ques_num, answer)

      if results == None:
        print "Failed to put answer"
        exit()
      else:
        print results

      raw_input("\nWait for your instructor to post next question before continuing\n")

