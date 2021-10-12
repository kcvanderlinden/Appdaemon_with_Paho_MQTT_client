import paho.mqtt.client as mqtt #import the client1
import re


############
def on_message(client, userdata, message):
    decoded_message=str(message.payload.decode("utf-8"))
    msg = re.sub('{|}|"', '', decoded_message)
    msg_ = re.split(':|,', msg)
    if 'action_duration' in msg_: # listening to de button press duration send by IKEA button (but is not registered as standard in HASS)
        button_duration = float(msg_[msg_.index('action_duration')+1]) # because the index of the actual duration is one more than the item called 'action_duration'
        print(button_duration)

broker_address="<IP of your MQTT broker>" 
client = mqtt.Client("Testing_Jupyter_labs") #create new instance
client.connect(broker_address) #connect to broker
client.on_message=on_message
client.loop_start() #start the loop
print("Subscribing to topic","zigbee2mqtt/IKEA_buttons_slaapkamer")
client.subscribe("zigbee2mqtt/IKEA_buttons_slaapkamer") # subscribe to specific mqtt topic
