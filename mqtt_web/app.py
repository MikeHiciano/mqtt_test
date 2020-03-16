from flask import Flask, jsonify, render_template, request
import paho.mqtt.publish as publish 

app = Flask(__name__)

broker_address = "10.0.0.13" # local broker ip
broker_port = 1883 # mqtt local brocker port
topic = 'sum_topic' # the topic

@app.route('/' ,methods=['GET','POST'])
def buttons():
    if request.method == 'POST':
        if request.form.get("on"):
            publish.single(topic,"on", hostname=broker_address,client_id='someone')
        
        elif request.form.get("off"):
            publish.single(topic,"off", hostname=broker_address,client_id='someone')

    return render_template("index.html")

if __name__ == "__main__":
    app.run()