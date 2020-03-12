import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

broker_address = "10.0.0.13"
broker_port = 1883
topic = 'sum_topic'

def on_message(client,userdata,message):
    print("mensaje recibido = ", str(message.payload.decode("utf-8")))
    if message.payload.decode("utf-8") == "on":
        GPIO.output(17, GPIO.HIGH)

    elif message.payload.decode("utf-8") == "off":
        GPIO.output(17, GPIO.LOW)

    # print("topic = ", message.topic)
    # print("Nivel de calidad [0|1|2] = ",message.qos)
    # print("Flag de retencion o nuevo? = ",message.retain)

if __name__ == '__main__':
    try:
        client = mqtt.Client()
        client.on_message = on_message
        client.connect(broker_address,broker_port, 60)
        client.subscribe(topic,0)
        client.loop_forever()
    
    except KeyboardInterrupt:
        GPIO.output(17, GPIO.LOW)
