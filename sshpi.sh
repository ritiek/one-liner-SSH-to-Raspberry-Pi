#!/bin/bash

# -------------------------------------------------------------
# replace the below with your weaved username & password
EMAIL="weaved_email"
PASS="weaved_pass"
PI_UID="raspberry_UID"
# -------------------------------------------------------------

TOKEN="$(curl -sS -X GET -H "content-type:application/json" -H "apikey:WeavedDemoKey\$2015" https://api.weaved.com/v22/api/user/login/$EMAIL/$PASS | cut -d'"' -f 8)"
HOST_IP="$(curl -sS -X GET ipinfo.io/ip/)"
HTTP_HOST="$(curl -sS -X POST -H "content-type:application/json" -H "apikey:WeavedDemoKey\$2015" -H "token:$TOKEN" --data '{"deviceaddress":"'$PI_UID'", "hostip":"$HOST_IP","wait":"true"}' https://api.weaved.com/v22/api/device/connect | cut -d'"' -f 22 | tr -d '\\')"
HTTP_HOST=${HTTP_HOST#"http://"}

HOST=$(echo $HTTP_HOST | cut -d':' -f 1)
PORT=$(echo $HTTP_HOST | cut -d':' -f 2)

if [ "$#" -ne 1 ]; then
    echo $HOST:$PORT
else
    echo $HOST -p $PORT
fi
