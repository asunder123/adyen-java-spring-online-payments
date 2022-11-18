#!/bin/bash
if [[ $? ]];
then
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
fi
echo "Set Env variables"
if [[ $? ]];
then 
 nohup ./gradlew bootRun &
fi
paymentappstatus= $(curl http://localhost:8080)
echo $paymentappstatus
echo "Payment app is ..."
if [[ $? ]];
then
  echo $paymentappstatus
  echo "Started gradle app"
fi  
if [[ $? ]];
then 	
 nohup  ./flask.sh  &
 checkoutstatus=$(curl http://localhost:8082/checkout)
 echo $checkoutstatus
fi
cardstatus=$(curl http://localhost:8081/card)
echo $cardstatus
echo "Flask apps started...." 
