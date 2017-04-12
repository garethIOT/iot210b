# Quizical Documentation

Quizical is an easy to use quiz API.


## APIs

Verb   | API                             | Description
------ | ------------------------------- | --------------------------------------------------------
GET    | /api/v1/login/{name}            | Login to Quizical. Receive a token for subsequent calls.
PUT    | /api/v1/profile                 | Used to change user password. Requires the login token.
GET    | /api/v1/student/question        | Get the current question with possible answers.
GET    | /api/v1/student/answer          | Your quiz results so far.
PUT    | /api/v1/student/answer          | Answer a question. Write once.
GET    | /api/v1/teacher/quiz            | Get the current quiz
PUT    | /api/v1/teacher/quiz            | Start a new quiz, move quiz on to next question, etc...
POST   | /api/v1/teacher/quiz            | Create a new quiz (clears all student answers)
DELETE | /api/v1/teacher/quiz            | Delete a quiz by name
GET    | /api/v1/teacher/results         | Results for all students
GET    | /api/v1/teacher/admin           | Get the list of students
POST   | /api/v1/teacher/admin           | Post a list of students


## CURL Script Examples

Curl is a general purpose tool. Below are the important bits.

```
  curl http://vcabin.swiftwater.lab/api/v1/student/{name}/question \
    -X verb \
    -H "Content-Type: application/json" \
    –d 'data'
    --verbose
```
It's available by default on the Mac (in the Terminal app), and in Windows via Cygwin or the Windows 10 Bash shell.

The --verbose is not needed, but can help understand HTTP, and can be useful for debugging.

The `Content-Type: application/json` header is not needed, as quizical.py assumes JSON.

For all examples below, the student is named "me" and the password "pass", and the login token is "xxxx".

The quizical.py application is assumed to be hosted at `https://frozen-castle-53348.herokuapp.com` (port 443).

### /api/v1/login/{name}

**Methods: GET**

Login to Quizical. Receive a token for subsequent calls

```
curl https://frozen-castle-53348.herokuapp.com/api/v1/login/me?pwd=pass
```

Returns a token, in JSON form, that must be used on all subsequent calls as a parameter.

```
{"token":"xxxx"}
```

If either the username or password is wrong, a `403 Forbidden` is returned.

### /api/v1/profile

**Methods: PUT**

Used to change user password. Requires the login token.

```
curl https://frozen-castle-53348.herokuapp.com/api/v1/profile?token=xxxx -X PUT -d '{"newpwd":"pass"}'
```


### /api/v1/student/question

**Methods: GET**

Get the current question with possible answers.

```
curl https://frozen-castle-53348.herokuapp.com/api/v1/student/question?token=xxxx
```

Returns the current quiz name and question, with all possible answers.

```
{"quizname":{"1":[ "ques"," a1"," a2"," a3"," a4" ]}}
```


### /api/v1/student/answer

**Methods: GET, PUT**

Returns your quiz results so far (GET), or allows a question to be answered (PUT).

Note: Each question can only be answered once (that is, if you PUT a second time it will return with the
answer unchanged).

```
# get answers so far
curl https://frozen-castle-53348.herokuapp.com/api/v1/student/answer?token=xxxx

# Answer question 2 with multiple choice 'D'
curl https://frozen-castle-53348.herokuapp.com/api/v1/student/answer?token=xxxx -X PUT -d '{"2":"D"}'
```

Returns `200 OK` and the following JSON:

```
{"correct":True,"results":"1/4","answers":{"1":"B","2":"D"}}
```

In the results above, the student has gotten one answer right out of 4.

If token is not valid, then returns `403 Forbidden`.


### /api/v1/teacher/quiz

**Methods: GET, PUT, POST, DELETE**

This API allows the teacher to view (GET), create (POST), start/continue (PUT) and delete (DELETE) quizzes.

```
# get the current quiz
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx

# create a new quiz
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx -X POST \
-d '{"python":{"questions":{"1":["ques"," A", "*B"],"2":["ques","*A"," B"]}}}'

# start the quiz
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx -X PUT -d '{"name":"python","question":"1","answer":"B","reset":true}'

# go to question 2 in quiz
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx -X PUT -d '{"question":"2","answer":"D"}'

# delete a quiz
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx -X DELETE -d '{"name":"python"}'
```

A quiz is defined by a unique name and a set of questions. Each question is an array, where element 0 is the
question, and all other elements are the answers. The 1st character of each answer must either be a space (for
incorrect answer) or with a '*' to indicate correct answer.

The '*' is removed (so the student doesn't know the correct answer) when viewing the question through the
`/api/v1/student/question` interface.

Returns 400 Bad Request if the quiz is not in the proper form.

### /api/v1/teacher/results

**Methods: GET**

This API allows the teacher to retrieve results of the quiz for all students. The option `anon`
allows the student names to be anonymous.

```
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/results?token=xxxx?anon=1
```
{
  "drewg": { "results":"4/4", "answers":{"1":"A","2":"C","3":"D","4":"C"}}
}

### /api/v1/teacher/admin

**Methods: GET**

Get the list of students (GET) or post a list of students (POST)

```
# get the list of students
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/admin?token=xxxx

# post a new list of students
curl https://frozen-castle-53348.herokuapp.com/api/v1/teacher/quiz?token=xxxx -X POST \
-d '{"name1":{"pwd":"pass","access":0,"token":"-","answers":"-"}}'
```

Returns JSON list of students.

```
{"name1":{"pwd":"pass","access":0,"token":"-","results":"-","answers":{}}}
```

Returns 400 Bad Request if student list is not in the proper form.
