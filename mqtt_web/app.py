from flask import Flask, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

broker_address = "localhost"
broker_port = 1883
topic = 'sum_topic'
