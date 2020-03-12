import time
import paho.mqtt.publish as publish 

broker_address = "10.0.0.13"
topic = "sum_topic"
while True:
    publish.single(topic,"on", hostname=broker_address,client_id='someone')
    time.sleep(1)
    publish.single(topic,"off", hostname=broker_address,client_id='someone')
    time.sleep(1)