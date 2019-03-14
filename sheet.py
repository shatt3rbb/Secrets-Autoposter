#!/usr/bin/python3

from __future__ import print_function
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json
import time
import datetime
import sys, os

def gacc_init():
    SCOPE = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    try:# Open setting file to get json file name and get absolute location
        lines = [] 
        f = open("settings.MIDGET","r+") #open for read/write
        for line in f:lines.append(line)
        f.close()
        json_name = lines[0].replace("json_file_name = '", "")
        json_name = json_name.replace("'", "")
        json_name = json_name.replace("\n", "")
        location = os.path.abspath(os.path.dirname(sys.argv[0]))+"\\" + json_name +".json"
    except:# if it fails ask user to provide it instead
        print("Couldn't read json location from settings file.")
        location = input("Please specify absolute location of your json: ")
    SECRETS_FILE = location
    SPREADSHEET = "an-tester"
    print("Initializing sheets...Please wait...")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SECRETS_FILE, SCOPE)
    gc = gspread.authorize(credentials)
    print("Sheet initialization done")
    return gc, SPREADSHEET

def list_available(gc):
    print("your available sheets are:")
    for sheet in gc.openall():
        print("{} - {}".format(sheet.title, sheet.id))
    return None

def create_frame(gc ,SPREADSHEET):
    workbook = gc.open(SPREADSHEET)
    #1 is used to indicate the first of your available sheets  as printed by the list_available function
    sheet = workbook.sheet1
    data = pd.DataFrame(sheet.get_all_records())
    return data, sheet
    
def view_answers(entries, SPREADSHEET, gc):
    print(data.head(int(entries)))

def view_single(entry, SPREADSHEET, gc):
    print(data.head(int(entry)))

def mark_uploaded(entry, bin_value, sheet):
    sheet.update_cell(entry, 6, bin_value)

def mark_timestamp(entry, sheet):
    sheet.update_cell(entry, 4, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def save_posted(entry, posted, sheet):
    sheet.update_cell(entry, 5, posted)

#The find_entry functions finds the first empty cell in the binary 
#column of the spread sheet and begins work from that point

def find_entry(data):
    i = 0
    while True:
        if((data['Binary'][i] != 0) and (data['Binary'][i] != 1)):
            break
        i+=1
    return i

def show_hashtag(data, entry):
    index = entry-1
    while (data['Hashtag'].iat[index]==''):
        index = index -1
    print("Current Hashtag is: ", data['Hashtag'].iat[index])
    return data['Hashtag'].iat[index]

def write_hashtag(entry, msg, sheet):
    sheet.update_cell(entry, 3, msg)
