#Rpi Flood Defense Project 2018
#By Daniel O'Brien
import RPi.GPIO as GPIO #imports hardware for the Raspberry Pi      
import subprocess  #The next modules are for sending emails and interacting with the internet ->
import smtplib
import socket  
from email.mime.text import MIMEText
from urllib.request import urlopen 
from time import sleep, strftime, time  #import timing
import getpass  #Saves passwords
import sys #Import System
import random  #imports random module
from datetime import datetime #imports a real clock
import webbrowser, os #imports Google Chrome Browser
import string #imports the English Alphabet
from tkinter import *   #These Modules both Import the Python GUI
from tkinter import messagebox  #Python GUI
from xml.dom import minidom  #Imports a XML Parser
from subprocess import call #Uploads to Dropbox from Pi
from turtle import * #For Animations
import matplotlib.pyplot as plt

myAPI = ""


GPIO.setmode(GPIO.BCM)

TRIG = 21      #port 21 is 'TRIG' for Ultrasonic Trigger
ECHO = 26      #port 26 is 'ECHO' for Ultrasonic Echo

GPIO.setup(TRIG,GPIO.OUT)  #sets up pin 21 to trigger a ping sound outwards
GPIO.setup(ECHO,GPIO.IN)   #sets up pin 24 to listen for an echo inwards

GPIO.output(TRIG, False)   #stops any errors

print ("Please Wait....")
sleep(2)

if GPIO.input(ECHO)!=1:
  break

def distcheck():  #function to measure distance
  count = 0
   
  while True:
    sleep(0.1)
    GPIO.output(TRIG, True)  #fires a pulse
    sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:  #measures time
      pulse_start = time()
      
    while GPIO.input(ECHO)==1:
      pulse_end = time()

    sleep(0.1)
    
    pulse_duration = pulse_end - pulse_start  #calculations

    distance = pulse_duration * 17150   #distance = time * speed of sound

    distance = round(distance, 2)       #rounds distance values off to 2 places

    return(distance)  

def send_mail_alert():  #function to send email alert
  to = 'dobg1.91@gmail.com'
  """
  gmail_user = input("Please enter full email address...")
  gmail_password = getpass.getpass()
  """
  smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.login(gmail_user, gmail_password)


  my_msg=("WARNING! Sea Levels have reached Critical Height! Beware of imminent Flooding! Water Height at " + str(mode) + "cm above normal sea level")
  msg=MIMEText(my_msg)

  msg['Subject']= 'Flood Warning'
  msg['From']= "Local Flood Defense System"
  msg['To'] = to
  smtpserver.sendmail(gmail_user, [to], msg.as_string())
  smtpserver.quit()
  print("Email sent to " + str(to))


def updateThingSpeak(): #sends data to a webpage
   print('starting...') 
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI  


   try:
       print("The mode being sent to the web is " + str(mode) + "cm") 
       f = urlopen(baseURL + "&field1=%s" % (str(mode))) 
       print (f.read()) 
       f.close() 
       sleep(30) #uploads sensor values every 30 secs
   except: 
       print('oops that did not work...')
      
#The Full Raspberry Pi Flood Defense System

print("Welcome to Raspberry Pi Flood Defense System")

  gmail_user = input("Enter your full email address")
  gmail_password = getpass.getpass(prompt="Type in your password")
  
  print("Please Wait.....")
  sleep(1)
  print("Taking Measuremnets NOW!")
  
  datacount = 0
