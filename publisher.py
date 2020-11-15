import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("localhost", 1883)
client.loop_start()

while True:
    temperature = b'p' * 1024 * 10
    (rc, mid) = client.publish("encyclopedia/temperature", str(temperature), qos=1)
    time.sleep(10)