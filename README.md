# webhook-listener

[![Build Status](https://travis-ci.org/LedForLike/webhook-listener.svg?branch=master)](https://travis-ci.org/LedForLike/webhook-listener/)


web server that handles webhook and push them into MQTT

## getting started:
### setup
to be able to communicate with MQTT you should have the following environemnt variable on your system:
* mqtt-host
* mqtt-user
* mqtt-pwd
* mqtt-port

you can grab the values from your [MQTTCloud](https://customer.cloudmqtt.com/) account

### install and run
run the following command to install project requirements

`pip install -r requirements.txt --cache-dir $HOME/.pip-cache`

run the following command to run application

`python .`

open browser locally at  [https://127.0.0.1:5000](https://127.0.0.1:5000)       
