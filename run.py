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
