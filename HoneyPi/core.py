#!/usr/bin/env python3.4
# encoding: utf-8
# creator: matsbauer
# date created: 24.01.2018


import json

if __name__ == "__main__":
    f = open('data.txxt','w')
    a = input('is python good?')
    f.write('answer:'+str(a))
    f.close()