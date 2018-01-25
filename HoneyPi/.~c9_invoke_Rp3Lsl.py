#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018


import json
import os.path

def create_json():
    d = {}
    honey = input("Would you like to tell me the name of your honey? ")
    means = input("How would you like to contact here, mail, telegram or sms? ")
    contact = input("Can you tell me here contact information for %s? " %means)
    #add to dic
    


def open_datafile():
    if os.path.isfile('data/data_file_23125129ox7.json') == True:
        data = json.load(open('data/data_file_23125129ox7.json'))
        honey = data["honey"]
        contact = data[data["means"]]
        print(contact)
        
    else: #create file
        f = open('data/data_file_23125129ox7.json','w')
        create_json()


if __name__ == "__main__":
    print("My name is main")
    open_datafile()