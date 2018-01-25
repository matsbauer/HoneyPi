#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018


import json
import os.path
import socket
from threading import Thread
import sys, re, time, sys
from random import randint

if sys.version_info >= (3, 0):
    from urllib.request import Request, urlopen
else:
    from urllib2 import Request, urlopen

#handler for raw_input Python 2/3
try: input = raw_input
except NameError: pass

json_path = 'data/data_file_23125129ox7.json'


def reload_ip(user):
    print("Hey %s, I still need to know where you work. "%user)
    if (input("Are you currently at work? Yes or no? ").lower() == "yes"):
        data = json.load(open(json_path))
        data["ip"] = socket.gethostbyname(socket.gethostname())
        with open(json_path, 'w') as fp:
            json.dump(data, fp)
    else:
        print("Alright, I will ask again next time you start me.")
        

def fill_json():
    d = {}
    user            =   input("What's your name? ")
    d['honey']      =   input("Would you like to tell me the name of your honey? ")
    means           =   input("How would you like to contact here, mail, telegram or sms? ")
    contact         =   input("Can you tell me here contact information for %s? " %means)
    d['max_time']   =   input("When are you expected to leave work? (eg. 17:30) ")
    d['message']    =   input("Would you like to tell me how to tell your honey that you are sorry? ")
    
    if (input("Are you currently at work? Yes or no? ").lower() == "yes"):
        #d['ip'] = socket.gethostbyname(socket.gethostname())
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        loc = json.load(response)
        d['ip'] = loc['ip'] #instead of socket, for people using external programming software s.a. c9.io
        d['city'] = loc['city']
    else:
        print("Alright, I will ask again next time you start me.")
        d['ip'] = "retry"
        
    d['user'] = user
    d['means'] = means.lower()
    d[means] = contact
    
    with open(json_path, 'w') as fp:
        json.dump(d, fp)
        
    return user
    

def open_datafile():
    if os.path.isfile(json_path) == True:
        data = json.load(open(json_path))
        user = data["user"]
        if data["ip"] == "retry":
            reload_ip(user)
        else:
            print("Welcome back to HoneyPi, %s"%user) 
        
    else: #create file
        f = open(json_path,'w')
        print("Welcome to HoneyPi. To get started I need a few information about your honey. This data is safe with you right here!") 
        print("")
        user = fill_json()
    
    return user
        
        
def notify():
    def send_it():
        print("sent")
        
    response = urlopen('http://ipinfo.io/json')

    if sys.version_info >= (3, 0): #python3 has a string not byte conversion problem in json.load.
        response = response.encode("utf-8") 
    
    #python3 response <http.client.HTTPResponse object at 0x7fdc7b20c940>
    #python2 reponse <addinfourl at 139895571535344 whose fp = <socket._fileobject object at 0x7f3bfa116ed0>>
    
    loc = json.load(response)
    current_ip = loc['ip']
    data = json.load(open(json_path))
    if(current_ip == data["ip"]):
        print("I notified %s"%data["honey"])
    else:
        if (input("Are you still at work? ").lower() == "yes"): 
            print("I notified %s"%data["honey"])


def notifier():
    data = json.load(open(json_path))
    notif_time = data['max_time'].split(":")
    while True:
        current_hour = int(time.strftime('%H')) + 1 #compensating 1 hour lag in c9
        current_minutes = int(time.strftime('%M'))
        minutes = (int(notif_time[0])-current_hour) * 60 + (int(notif_time[1]) - int(current_minutes))
        try:
            if minutes < 10:
                if minutes > 0:
                    print("Only %s minutes to go!"%minutes)
                    time.sleep(((minutes)*60))
                else:
                    extra_time = randint(0,0)
                    print("It's time to notify, but I'll be waiting another %s minutes - so nobody notices me"%(extra_time))
                    time.sleep(extra_time*60) #varies the notification time, so honey won't notice.
                    notify()
                    break
            
            else:
                print("Time to wait - %s to go"%minutes)
                time.sleep((minutes - 10)*60)
                continue
        except KeyboardInterrupt:
            raise 
    

if __name__ == "__main__":
    user = open_datafile() #JSON exists or has been created
    data = json.load(open(json_path))
    print("I actived the notifier for you, %s will receive a message if you are in at work in %s after %s"%(data['honey'], data['city'], data['max_time']))
    try: 
        Thread(target=notifier, args=()).start()
    except KeyboardInterrupt:
        raise
    except TypeError:
        print("You seem to be over your latest work time already!")