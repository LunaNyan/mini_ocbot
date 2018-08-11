#!/usr/bin/python3

import random
import re

#Global
versiontext = "1.0.0"

#mini db
m_emoticon = ['>_<', '>ㅅ<', '>ㅁ<', '//ㅅ//']
m_emoticon_tail = ['', '~', '~☆', '~//']

t_blush = ['흐와앗', '후와아', '후에엣', '하와와']
t_blush_tail = ['..', '~', '..!']

t_surprised = ['흐엣', '흐왓', '후냣']
t_surprised_tail = ['..!', '!', '..']

t_pat = ['히냐앙', '후와앗', '헤헤']

#Fundamental variables
outp = ""
pat_firsttime = 0
conv_save = 0


#Startup
print ("미니 오너캐봇 v" + versiontext)
print ("by 루냥이, at 20180811, https://keybase.io/lunanyan")
print (" ")
print ("지원 가능한 대화어는 help를 입력하십시오.")
print (" ")

logfoo = open("conv.txt", "w")
logfoo.close()

#main loop
while 1:
	inp = input (">>>")
	if inp == "exit":
		break
	elif inp == "help":
		print ("지금은 아무 말이나 써도 똑같이 반응합니다")
		print (" ")
		print ("help	해당 도움말을 표시합니다")
		print ("save	대화 내역 자동 저장을 토글합니다")
		print ("exit	애플리케이션을 종료합니다")
	elif inp == "save":
		if conv_save == 0:
			print ("대화 내역을 자동 저장합니다")
			print ("대화 내역은 conv.txt에 저장됩니다")
			conv_save = 1
		else:
			print ("대화 내역을 자동 저장하지 않습니다")
			conv_save = 0
	else:
		a = random.randrange(1,3)
		if a == 1:
			if pat_firsttime == 0:
				outp = random.choice(t_surprised) + random.choice(t_surprised_tail)
				pat_firsttime = 1
			else:
				outp = random.choice(t_blush) + random.choice(t_blush_tail)
		elif a == 2:
			outp = random.choice(m_emoticon) + random.choice(m_emoticon_tail)
		else:
			outp = random.choice(t_pat)+'~'
		print (outp)
		if conv_save == 1:
		        logf = open("conv.txt", "a")
        		logf.write(">>>" + inp + "\n" + outp + "\n")
        		logf.close()
