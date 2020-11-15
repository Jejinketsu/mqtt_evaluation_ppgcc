import paho.mqtt.publish as publish
import time

msgs = [{'topic':"encyclopedia/temperature", 'payload': b'p' * 1024 * 20, 'qos': 1, 'retain': True},
    {'topic':"encyclopedia/temperature", 'payload': b'p' * 1024 * 20, 'qos': 1, 'retain': True},
    {'topic':"encyclopedia/temperature", 'payload': b'p' * 1024 * 20, 'qos': 1, 'retain': True},
    {'topic':"encyclopedia/temperature", 'payload': b'p' * 1024 * 20, 'qos': 1, 'retain': True},
    {'topic':"encyclopedia/temperature", 'payload': b'p' * 1024 * 20, 'qos': 1, 'retain': True}]

while True:
    publish.multiple(msgs, hostname="localhost", port=1883)
    time.sleep(1)