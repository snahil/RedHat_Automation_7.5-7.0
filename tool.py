import os
import subprocess
import numpy
import cv2
import requests
os.system("tput setaf 3")
print ("\t\t\t WELCOME TO MY REDHAT AUTOMATION TOOL")
os.system ("tput setaf 2")
print ("\t\t\t ------------------------------------")

response = input("DO YOU WANT TO GET ACCESS remote OR local:    ")
if (response == "local"):
        print("\n\n Functionality Provided")
        print("""
        PRESS 1: To Check The Date
        PRESS 2: To  Run Cal
        PRESS 3: File Tool's i.e creating file/ deleating file
        PRESS 4: User Tool's i.e adding a new user/ deleating a user
        PRESS 5: Capturig Picture through a webcam
        PRESS 6:
        PRESS 7:
        PRESS 8:
        PRESS 9:
        PRESS 10:
        PRESS 11: To Exit The Tool
        """)

        num=int(input())                
        if(num==1):
            x=subprocess.getoutput("date")
            print(x)
        elif(num==2):
            x=subprocess.getoutput("cal")
            print(x)   
        elif(num==3):
            print("""
            PRESS 1: TO ADD A NEW FILE   
            PRESS 2: TO REMOVE A FILE
            """)
            choice=int(input())
            if(choice==1):
                      f_name=input("Enter the file you wish to create")   
                      f_location=input("Enter the location of file where you want to place it")
                      handle=subprocess.getstatusoutput("touch {}/{}".format(f_location,f_name))
            if(handle[0]==0):
                          print("File Created Sucessfully @!!!!!") 
                          res = input("Open the file? Y/N")
                          if(res=="yes" or res=="y"):
                              os.system("gedit %s.py"%f_name)
        elif(num==5)
             cap=cv2.VideoCapture(0) # O is used to access the inbuild web can as 1 is used for the external web cam
             ret,photo = cap.read()
             cv2.imwrite('/root/Desktop/snahil1.png',photo)
        else:
            print("Failed to create file. Description: {}".format(handle[1]))
            os.system("tput setaf 4")                  
            