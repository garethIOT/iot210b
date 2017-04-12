#!/usr/bin/python
# =============================================================================
#        File : simpleserver.py
# Description : simple server echos the input
#      Author : Drew Gislsason
#        Date : 4/6/2017
# =============================================================================
import random
import string
import json
import sys

PORT = 5000

from flask import Flask, request

# ============================== APIs ====================================

# create the global objects
app = Flask(__name__)

@app.route("/my/api", methods=['GET', 'PUT', 'POST', 'DELETE'])
def ApiV1Echo():

  rsp_data = "Echo:\nMethod: "

  if request.method == 'GET':
    rsp_data += "GET"
  elif request.method == 'PUT':
    rsp_data += "GET"
  elif request.method == 'POST':
    rsp_data += "POST"
  elif request.method == 'DELETE':
    rsp_data += "DELETE"

  rsp_data += "\nArgs: "
  for arg in request.args:
    rsp_data += str(arg) + ":" + request.args[arg] + " "

  rsp_data += "\nData:\n"
  rsp_data += request.get_data()
  rsp_data += "\n"

  return rsp_data, 200


# ============================== Main ====================================

if __name__ == "__main__":

  app.debug = True
  app.run(host='0.0.0.0', port=PORT)
