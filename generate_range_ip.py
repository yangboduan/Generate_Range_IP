#!/usr/bin/python
#encoding=utf-8
import sys

IPA=sys.argv[1]
IPB=sys.argv[2]

def myint(x):
    return int(x)


IPA1,IPA2,IPA3,IPA4=map(myint,IPA.split("."))
IPB1,IPB2,IPB3,IPB4=map(myint,IPB.split("."))


#如果从第四段开始不一样
def generate_D():
    for D in  range(IPA4,IPB4+1):
        print str(IPA1)+"."+str(IPA2)+"."+str(IPA3)+"."+str(D)

#如果从第三段开始不一样
def generate_C():
    for C in range(IPA3,IPB3+1):
        if C==IPA3:
            startD=IPA4
            endD=256

        elif C==IPB3:
            startD=0
            endD=IPB4+1
       
        else:
           startD=0
           endD=255
        
        for D in range(startD,endD):
            print str(IPA1)+"."+str(IPA2)+"."+str(C)+"."+str(D)

def generate_IP():
   if IPA3!=IPB3:
       generate_C()
   else:
       generate_D()

generate_IP()

   
