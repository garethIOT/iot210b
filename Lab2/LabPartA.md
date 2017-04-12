[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

# Lab2 Part A - HTTP, REST, URLs and Curl

In this section of the lab you will

* Learn about REST and HTTP and URLs
* Learn to use curl with APIs and HTTP programs

These apps can be run from the Raspberry Pi in terminal windows, or on your PC

## Pull the Repo

If new, use git clone (I suggest starting in your Documents/Git folder)

```
pi$ cd ~/Documents/Git
pi$ git clone https://Gislason@gitlab.com/Gislason/iot-210B-student.git
pi$ cd iot-210B-student/Lab2/src
```

If you've already cloned (made a copy) of the repository, then just pull updates:

```
pi$ cd ~/Documents/Git/iot-210B-student
pi$ git pull
pi$ cd Lab2/src
```

## Curl

Curl is a general purpose tool. Below are the important bits.

```
  curl https://https:frozen-castle-53348.herokuapp.com/api/v1/student/{name}/answer \
    -X POST \
    -H "Content-Type: application/json" \
    –d '{"1":"A"}'
    --verbose
```

The --verbose is not needed, but can help understand HTTP, and can be useful for
debugging.

One header is Content-Type, for example `Content-Type: application/json`. This may be needed with
JSON APIs. See Wikipedia for a list of HTTP headers. Their use is dependant on Host application.

A very useful tool for checking JSON for correctness is online at [JSONLint](http://jsonlint.com)

## Experiment with Curl

Go ahead and experiment with curl. Try using curl with ipv4_tcp_server.py

In one terminal window, run (see Lab2/src):

```
pi$ python ipv4_tcp_server.py
```

In another terminal window.

```
pi$ curl localhost:5000/
pi$ curl localhost:5000/my/api/path?myparam=hello -X PUT -d 'hello world'
```

Why doesn't curl exit? (you can exit curl with ctrl-c)

## Verify Flask Runs on your System

If you've done the homework for Week1, you have Flask (a Web/API Server framework for Python)
installed. If you haven't, now is a good time to go finish that task.

In a terminal window, run (Lab2/src))

```
pi$ python simpleserver.py
```

In another terminal window.

```
pi$ curl localhost:5000/my/api
pi$ curl localhost:5000/my/api?hello=world -X POST -d 'Flask is cool'
```

experiment with all verbs (GET, PUT, POST, DELETE)


[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
