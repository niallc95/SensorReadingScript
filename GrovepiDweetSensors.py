import dweepy
import time
import psutil
import random
import time
import datetime
import grovepi
import math

#Import configuration file 
import config

#Student name: Niall Curran
#Student Number: x13440572
#Submission 1
#Description: Read sensor data from raspberry pi and grove unit and submit to dweet.io

# Grove Pi Connections
light_sensor = 0        # Grove port A0
sound_sensor = 1        # Grove port A1
temperature_and_humidity_sensor = 2  # Grove port D2

#Get current time 
now = datetime.datetime.now()

def getTemperature():
    [temp,hum] = grovepi.dht(temperature_and_humidity_sensor,0)
    return temp 

def getHumidity():
    [temp,hum] = grovepi.dht(temperature_and_humidity_sensor,0)
    return hum

def getSound():
    return grovepi.analogRead(sound_sensor)
   
def getLight():
    return grovepi.analogRead(light_sensor)

def getTime():
    return now.hour,now.minute,now.second

    
#Send information to specific dweet thing
def post(readings):
    thing = config.thing
    print dweepy.dweet_for(thing, readings)
 
#Get all information and store in a dictionary
def getReadings():
    dict = {}
    dict["Temperature"] = getTemperature();
    dict["Humidity"] = getHumidity();
    dict["Sound"] = getSound()
    dict["Light"] = getLight()
    dict["Description"] = "IoT Submission 1"
    dict["Time"] = getTime()
    return dict

#Dweet new data every 6 seconds 
while True:
    #error handling in case of issues with grove pi
    try: 
        dict = getReadings();
        post(dict)
    
        #Duration to sleep in seconds before gathering data again and Dweeting
        time.sleep(6)
    except IOError:
        print(config.IOError)

    except KeyboardInterrupt:
        exit()

    except:
        print(config.PiError)
