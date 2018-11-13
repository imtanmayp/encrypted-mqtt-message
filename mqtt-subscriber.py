import paho.mqtt.client as mqtt
 
MQTT_SERVER = "172.16.50.177"
MQTT_PATH = "t"
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  #print('decrypting:',msg)
  a=(msg.topic+" "+str(msg.payload))
  print a
  key = 'abcdefghijklmnopqrstuvwxyz'
  result = ''
  for l in a:
        try:
            i = (key.index(l) - 5) % 26
            result += key[i]
        except ValueError:
            result += l
        decrypt=result
  #print(decrypt.topic+" "+str(decrypt.payload))
  print (decrypt)
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
