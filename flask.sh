#!/bin/bash
cd ~/adyen*/src/main/python
export FLASK_APP="card.py"
if [[ $? ]];
then	
 nohup flask run -h localhost -p 8081 &
fi
if [[ $? ]];
then 
 cd ~/adyen*/src/main/python
 echo $pwd
 export FLASK_APP="checkout.py"
 nohup flask run -h localhost -p 8082 &
 echo "Flask app2 started..."
fi
