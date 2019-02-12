#!/bin/usr/python36


#import pandas
import os
#import requests
#import numpy as np
#import cv2


print("WELCOME TO MY TOOL FOR REDHAT AUTOMATION")
print("========================================")
print ("USING THE TOOL LOCALY OR REMOTELY")
ch=input()
if ch == 'localy'
print("""
    PRESS 0 FOR HADOOP CLUSTER FORMATION
    press 1 FOR SOFTWARE USE AND FUNCTIONALITY
    PRESS 2 FOR LIVE STREAMING FROM MOBILE
    PRESS 3 FOR FACE RECOGIANTION
    PRESS 10 FOR EXIT THE TOOL
      """)
if ch == '1'
print (""" 
       PRESS A FOR INSTALLING A SOFTWARE PACKAGE WITH RPM PACKAGE MANAGER.
       PRESS B FOR INSTALLING A SOFTWARE PACKAGE WITH YUM.
       PRESS C FOR INSTALLING A SOFTWARE PACKAGE USING PIP-2 FROM THE WEB.
       PRESS D FOR INSTALLING A SOFTWARE PACKAGE USING PIP-3 FROM THE WEB.
       PRESS E FOR UNINSTALL A SOFTWARE PACKAGE FROM THE SYSTEM.
       PRESS F FOR  KNOWLEDGE BASE.
       PRESS X FOR RETURNING TO THE MAIN MENU.
       PRESS Y FOR EXIT THE TOOL.
        """)


x = raw_input ("Enter Your Choice")



if ch == 'A'
            m = raw_input("Enter The name of the tool which you want to install  :         ") 
            n = raw_input("Enter the path of the tool i.e /root/Desktop/hadoop.rpm")
            os.system ( 'rpm -ivh' + m)  
if ch == 'B' 
            m = raw_input("Enter the name of the software which you want to install")
            os.system ( ' yum ' + m)





            


