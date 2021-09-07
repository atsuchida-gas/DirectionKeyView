# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials 


up_GPIO = 14 
down_GPIO = 24 
right_GPIO = 15
left_GPIO = 23 

GPIO.setmode(GPIO.BCM)
GPIO.setup(up_GPIO, GPIO.IN)
GPIO.setup(down_GPIO, GPIO.IN)
GPIO.setup(right_GPIO, GPIO.IN)
GPIO.setup(left_GPIO, GPIO.IN)

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('spreadsheet-test-324604-bca8e2276e01.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = '1bAbXtoHRG3P1hA0sol9I9NoE32Sw7NB5N7EO57PLdYI'
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

def printdata():
    if GPIO.input(up_GPIO) == GPIO.HIGH:
        print("up")
    elif GPIO.input(down_GPIO) == GPIO.HIGH:
        print("down")       
    elif GPIO.input(right_GPIO) == GPIO.HIGH:
        print("right")        
    elif GPIO.input(left_GPIO) == GPIO.HIGH:
        print("left")

def count_up():
    if GPIO.input(up_GPIO) == GPIO.HIGH:
        import_value_up = int(worksheet.acell('A2').value)
        export_value_up = import_value_up+1
        worksheet.update_cell(2,1, export_value_up)
        
def count_down():
    if GPIO.input(down_GPIO) == GPIO.HIGH:
        import_value_down = int(worksheet.acell('B2').value)
        export_value_down = import_value_down+1
        worksheet.update_cell(2,2, export_value_down)
        
def count_right():
    if GPIO.input(right_GPIO) == GPIO.HIGH:
        import_value_right = int(worksheet.acell('C2').value)
        export_value_right = import_value_right+1
        worksheet.update_cell(2,3, export_value_right)
        
def count_left():
    if GPIO.input(left_GPIO) == GPIO.HIGH:
        import_value_left = int(worksheet.acell('D2').value)
        export_value_left = import_value_left+1
        worksheet.update_cell(2,4, export_value_left)
        
def count_clean():
    worksheet.update_cell(2,1, 0)
    worksheet.update_cell(2,2, 0)
    worksheet.update_cell(2,3, 0)
    worksheet.update_cell(2,4, 0)
        

  
try:
    print('--- start program ---')
    while True:
        printdata()
        count_up()
        count_down()
        count_right()
        count_left()


 
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    count_clean()
    print('--- stop program ---')
