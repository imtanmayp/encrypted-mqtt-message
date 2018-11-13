import paho.mqtt.publish as publish
 
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
msg="hello"
key = 'abcdefghijklmnopqrstuvwxyz'
result = ''
for l in msg.lower():
        try:
            i = (key.index(l) + 5) % 26
            result += key[i]
        except ValueError:
            result += l
        enmsg=result.lower()
print("plain text",msg)
print('encrypted',enmsg)
publish.single(MQTT_PATH, enmsg, hostname=MQTT_SERVER)
