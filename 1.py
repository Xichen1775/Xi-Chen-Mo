# -*- coding: utf-8 -*-
from api import *
from datetime import datetime
import time,random,re,six,ast,pytz,timeit,atexit,pafy,youtube_dl
import sys,os
import json,codecs,string
from bs4 import BeautifulSoup;import requests,urllib
import subprocess;import threading as td
#===============================================================================
start = time.time()
cl = LINE()
oepoll = OEPoll(cl)
clMid = cl.profile.mid

temp = json.load(codecs.open('temp.json','r','utf-8'))
ban = json.load(codecs.open('ban.json','r','utf-8'))

Language_change(input('please select the language: '))

cl.log("login success.")
#..............................
tok = []
td_append(50)
#===============================================================================
class Main():
    def Command(op):
        try:
            if op.type is 0:
                print("[Command] Op 0.")
                return
            if op.type is 25 or 26:
                msg = op.message
                sender = op.message._from

        except Exception as e:
            logError(e)
    def LineBot(op):
        try:
            if op.type is 0:
                print("[Bot Process] Op 0.")
                return
            if op.type is 5:

            if op.type is 11:

            if op.type is 13:

        except Exception as e:
            logError(e)
#===============================================================================
class Line_Bot_Support():
    def Language_change(input):
        if input is None:
            print('[Language_change] defult setting.')
            reply = json.load(codecs.open('ren.json','r','utf-8'))
            command = json.load(codecs.open('cen','r','utf-8'))
        if str(input).lower() in ['zh','zhong wen','chinese','中文','中']:
            print('[Language_change] chinese.')
            reply = json.load(codecs.open('rch','r','utf-8'))
            command = json.load(codecs.open('czh','r','utf-8'))
        if str(input).lower() in ['en','english','英文','英']:
            print('[Language_change] english')
            reply = json.load(codecs.open('ren.json','r','utf-8'))
            command = json.load(codecs.open('cen','r','utf-8'))
class Threading_Line_for_bot():
    def td_append(num):
        if len(num) not is (None or 0):
            print('[Append Thread] %s Lines.' %len(num))
            while len(num):
                td.Thread(target=tok.append,args=(cl.authToken)).start()
        else:print('[Append Thread] Empty Line.')
        print("[Append Thread] Now You got %s Lines." % len(num))
