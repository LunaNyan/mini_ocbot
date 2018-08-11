#!/usr/bin/python3

import random
import re

#Global
versiontext = "1.0.0"

#mini db
m_emoticon = ['>_<', '>ㅅ<', '>ㅁ<', 'ㅇㅅㅇ']
m_emoticon_tail = ['', '~', '~☆', '~//']

t_blush = ['흐와앗', '후와아', '후에엣', '하와와']
t_blush_tail = ['..', '~//ㅅ//', '..!']

t_surprised = ['흐엣', '흐왓', '후냣']
t_surprised_tail = ['..!', '!', '..']

t_pat = ['히냐앙', '후와앗', '헤헤']



#Startup
print ("미니 오너캐봇 v" + versiontext)
print ("by 루냥이, at 20180811, https://keybase.io/lunanyan")
print (" ")
print ("지원 가능한 대화어는 help를 입력하십시오.")
print (" ")

#main loop
while 1:
	inp = input (">>>")
	if inp = exit:
		break
	
