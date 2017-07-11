#!/bin/python

import datetime
import base64
import sys
import errno
import httplib2
from urllib2 import urlopen
import json
from json import dumps
import os
import time
import socket

apiMethod = "https://"
apiServer = "api.weaved.com"
apiVersion = "/v22"
apiKey = "WeavedDemoKey$2015"

# -------------------------------------------------------------
# replace the below with your weaved username & password
EMAIL = "weaved_email"
PASS = "weaved_pass"
# replace this with the actual UID of your Raspberry Pi
PI_UID = "raspberry_UID"
#--------------------------------------------------------------

def proxyConnect(UID, token):
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    my_ip = urlopen('http://ipinfo.io/ip/').read()
    proxyConnectURL = apiMethod + apiServer + apiVersion + "/api/device/connect"

    proxyHeaders = {
                'Content-Type': content_type_header,
                'apikey': apiKey,
                'token': token
            }

    proxyBody = {
                'deviceaddress': UID,
                'hostip': my_ip,
                'wait': "true"
            }

    response, content = http.request( proxyConnectURL,
                                          'POST',
                                          headers=proxyHeaders,
                                          body=dumps(proxyBody),
                                       )
    try:
        data = json.loads(content)["connection"]["proxy"]
	data = data.replace('http://', '')
        return data
    except KeyError:
        print "Key Error exception!"

if __name__ == '__main__':
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"

    loginURL = apiMethod + apiServer + apiVersion + "/api/user/login"

    loginHeaders = {
                'Content-Type': content_type_header,
                'apikey': apiKey
            }
    try:
        response, content = http.request( loginURL + "/" + EMAIL + "/" + PASS,
                                          'GET',
                                          headers=loginHeaders)
    except:
        print "Server not found.  Possible connection problem!"
        exit()

    try:
        data = json.loads(content)
        if(data["status"] != "true"):
            print "Can't connect to Weaved server!"
            exit()

        token = data["token"]
    except KeyError:
        print "Connection failed!"

    host = proxyConnect(PI_UID, token)
    trim = host.split(':')
    ip = trim[0]
    port = trim[1]
    os.system('ssh pi@' + ip + ' -p ' + port)
