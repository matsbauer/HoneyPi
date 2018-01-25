#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018


import json
import os.path
import socket

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
    print("Welcome to HoneyPi. To get started I need a few information about your honey. This data is safe with you right here!") 
    print("")
    d['user']       =   input("What's your name? ")
    d['honey']      =   input("Would you like to tell me the name of your honey? ")
    means           =   input("How would you like to contact here, mail, telegram or sms? ")
    contact         =   input("Can you tell me here contact information for %s? " %means)
    d['max_time']   =   input("When are you expected to leave work? (eg. 17:30) ")
    d['message']    =   input("Would you like to tell me how to tell your honey that you are sorry? ")
    
    if (input("Are you currently at work? Yes or no? ").lower() == "yes"):
        d['ip'] = socket.gethostbyname(socket.gethostname())
    else:
        print("Alright, I will ask again next time you start me.")
        d['ip'] = "retry"
        
    d['means'] = means.lower()
    d[means] = contact
    
    with open(json_path, 'w') as fp:
        json.dump(d, fp)
    

def open_datafile():
    if os.path.isfile(json_path) == True:
        data = json.load(open(json_path))
        if data["ip"] == "retry":
            reload_ip(data["user"])
        honey = data["honey"]
        contact = data[data["means"]]
        
    else: #create file
        f = open(json_path,'w')
        fill_json()
        

if __name__ == "__main__":
    print("My name is main")
    open_datafile()