#!/usr/bin/python
# =============================================================================
#        File : http_client.py
# Description : Allows sending a verb with data via HTTP over TCP/IP
#      Author : Drew Gislsason
#        Date : 3/8/2017
# =============================================================================
import httplib
import base64
import sys

# use this client for sending to 

URL = "127.0.0.1"
PATH = '/api/v1/login/'
PORT = 5000

name = raw_input('Enter username (e.g. me): ')
pwd  = raw_input('Enter password (e.g. pass): ')

# path (aka route) with options (aka query, arguments)
path_with_opts = PATH + name + '?pwd=' + pwd

conn = httplib.HTTPConnection(URL, 5000)

conn.request('GET', path_with_opts )
r1 = conn.getresponse()
print "status " + str(r1.status) + ", reason " + str(r1.reason)
data1 = r1.read()
print "data: " + str(data1)
conn.close()
