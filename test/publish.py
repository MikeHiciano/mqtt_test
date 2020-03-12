import paho.mqtt.publish as publish 

broker_address = "10.0.0.13"
topic = "sum_topic"
publish.single(topic,"hello another", hostname=broker_address,client_id='someone')