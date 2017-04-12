[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

A Special Thank You to Josh Welschmeyer for the Heroku instructions

# Homework

The homework is to set up your own Heroku account and host quizical.py (or your own app).
Provide a link to your instructor.

**Important:** create a NEW folder NOT inside your student repository, as you can't have a git
repository inside another one.

```
  my_student_git_repo
  my_heroku_git_repo
```

Heroku URLs use two random words, and a random # (e.g. frozen-castle-53348)

# Installing and Running Heroku Steps in Detail

## Step 1) Sign Up / Verify Account etc.

[http://www.heroku.com](http://www.heroku.com)

## Step 2) Setting up local machine

### Install Python 2.7

- Windows [http://docs.python-guide.org/en/latest/starting/install/win/](http://docs.python-guide.org/en/latest/starting/install/win/)

- OSX [http://docs.python-guide.org/en/latest/starting/install/osx/](http://docs.python-guide.org/en/latest/starting/install/osx/)

- Linux [http://docs.python-guide.org/en/latest/starting/install/linux/](http://docs.python-guide.org/en/latest/starting/install/linux/)


### Install Depenedencies

#### Install Pip

Download [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)

- Windows / OSX `python get-pip.py`

- Linux (sudo apt-get install python-pip)

#### Other Dependencies

- sudo pip install flask
- sudo pip install Flask-HTTPAuth

#### Install heroku CLI
 
[https://devcenter.heroku.com/articles/heroku-cli#download-and-install](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

`$ heroku login`

## Step 3) Create Heroku App

```bash
$ heroku create --buildpack heroku/python
Creating app... done, thawing-hamlet-90035
https://thawing-hamlet-90035.herokuapp.com/ | https://git.heroku.com/thawing-hamlet-90035.git

$ git init
Initialized empty Git repository in <PATH>.git/

$ heroku git:remote -a thawing-hamlet-90035
set git remote heroku to https://git.heroku.com/thawing-hamlet-90035.git
```

## Step 4)

Define Procfile

```text
web: gunicorn app:app --log-file=-
```

Define requirements.txt

```text
Flask
Flask-HTTPAuth
gunicorn
```

## Step 5)

```bash
git add
git commit
git push heroic master
```

-----

## Notes:

**using the heroku cli**

```bash
$ heroku help
$ heroku apps                # list all apps
heroku logs                  # display logs for your app
heroku config:set KEY=VALUE  # set config variable
heroku config:get KEY        # get config variable
heroku config:unset KEY      # unset config variable
```

[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
