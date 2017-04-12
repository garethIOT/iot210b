[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

Lab2 Part B - Quizical, A more complicate API, with secure tokens

# Quizical

Quizical is a multiple-choice quiz engine using Python and Flask. It's
designed to instruct how APIs can be designed, and how to use all HTTP VERBs
in actual commands. It will later be used to host an application on the
internet.

Go to the GitLab Wiki to see the Quizzical documentation.

## Overview

The instructor will run Quizical on his machine for those working in the classroom. Everyone
on the local network should be able to participate.

If you are working remotely, or wish to run your own quiz, run quizzical yourself (it can
run in the raspberry PI). See Remote Instructions.


## Quiz Client

Open another terminal window for the Client application, quiz.py

```
pi$ cd ~/Documents/Git/iot-210B-student/Lab2/src
pi$ python quiz.py
```

You should log in with your firstname, last initial, and your lastname as your password. For
example, if your name is matt smith, your username is `matts` and your password is `smith`.

```
Enter Username (e.g. me): me
Enter Password (e.g. pass): pass
token=smUG5gJ83hxiOgQFRXv5

Quiz: osi7layer question: 1
What best describes the PHY layer?
 A. It is the physical modulation layer (e.g. wireless or wired)
 B. It is for medical (physician) devices
 C. It is for signal quality (fidelity)
 D. It is the study of plants (phytology)
Your answer: A

Wait for your instructor to post the next question
```

Make sure wait after posting each answer, otherwise, the quiz will stop. This isn't a rich UI
quiz engine, just a simple demonstration.

# Remote Instructions

In one terminal window run the Quizical Server.

```
pi$ cd ~/Documents/Git/iot-210B-student/Lab2/src
pi$ python quizical.py
```

If you want to move on to the next question, you must act as your own instructor. Use
curl to do this in yet another terminal window: Copy the token into to use with curl.

```
pi$ curl localhost:5000/api/v1/login/drewg?pwd=gislason
pi$ curl localhost:5000/api/v1/teacher/quiz?token=smUG5gJ83hxiOgQFRXvF -X PUT \
-d '{"question":"2","answer":"C"}'
```

To end the quiz, use {"name":"done"} for the data.

To see quiz results for all students, use:

```
$pi curl localhost:5000/api/v1/teacher/results?token=smUG5gJ83hxiOgQFRXvF
```

FYI, `localhost` and `127.0.0.1` are the same.


## Try Making Your own Quiz or adding your own users

Modify quizical.py to contain your own multiple choice quiz.

For now, you'll need to modify the quizical.py program. However, the API could
be extended to POST new quizzes and to add/remove users.

Host quizical on your own PI (see instructions for remote use), and try out your
quiz.


[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
