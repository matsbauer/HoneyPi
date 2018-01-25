#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018


import json
import os.path

json_path = 'data/data_file_23125129ox7.json'

def fill_json():
    d = {}
    print("Welcome to HoneyPi. To get started I need a few information about your honey. This data is safe with you right here!") 
    print("")
    honey = raw_input("Would you like to tell me the name of your honey? ")
    means = raw_input("How would you like to contact here, mail, telegram or sms? ")
    contact = raw_input("Can you tell me here contact information for %s? " %means)
    max_time = raw_input("When are you expected to leave work? (eg. 17:30)")
    
    d['honey'] = honey
    d['means'] = means.lower()
    d[means] = contact
    d['max_time'] = max_time
    
    with open(json_path, 'w') as fp:
        json.dump(d, fp)
    

def open_datafile():
    if os.path.isfile(json_path) == True:
        data = json.load(open(json_path))
        honey = data["honey"]
        contact = data[data["means"]]
        
    else: #create file
        f = open(json_path,'w')
        fill_json()
        

if __name__ == "__main__":
    print("My name is main")
    open_datafile()