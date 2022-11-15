#!/bin/bash

export ADYEN_API_KEY="key-1"
export ADYEN_MERCHANT_ACCOUNT="acc1"
export ADYEN_CLIENT_KEY="clientkey1"
export ADYEN_HMAC_KEY="hmackey"
export ADYEN_KEY="hmackwweyXXX"
set ADYEN_API_KEY="key-1"
set ADYEN_MERCHANT_ACCOUNT="acc1"
set ADYEN_CLIENT_KEY="clientkey1"
set ADYEN_HMAC_KEY="hmackey"
set ADYEN_KEY="hmackwweyXXX"
echo "Set Env variables"
if [[ $? ]];
then 
 nohup ./gradlew bootRun
 echo "Start gradle app" 
 cd ~/adyen*/src/main/python
 echo "Path is\n" 
 echo $pwd
 export FLASK_APP="checkout.py"
 echo "init flask app" 
 nohup flask run -h localhost -p 8081
 echo "Flask app running on same port"
fi
