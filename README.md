# Webhook Listener

[![Build Status](https://travis-ci.org/LedForLike/webhook-listener.svg?branch=master)](https://travis-ci.org/LedForLike/webhook-listener/)

The simple HTTP server that exposes webhook and push messages into MQTT

### Setup
To be able to communicate with MQTT you should have the following environment variables on your system:
* mqtt-host
* mqtt-user
* mqtt-pwd
* mqtt-port

You can grab the values from your [MQTTCloud](https://customer.cloudmqtt.com/) account.

### Install and run

Run the following command to install project requirements:
```
pip install -r requirements.txt --cache-dir $HOME/.pip-cache
```

ant the following command to run application:
```
python .
```


