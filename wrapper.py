#!/usr/bin/python3

import sheet
import fb_autoposter
import pandas
import time

def initialize():
    gc, spreadsheet = sheet.gacc_init()
    sheet.list_available(gc)
    print('-------------------------')
    data, worksheet = sheet.create_frame(gc ,spreadsheet)
    key = input("Input your facebook user access api key: ")
    
    #Autoposter initialization
    
    print("Initializing facebook poster... Please wait....")
    cfg = fb_autoposter.init_token(key)
    api = fb_autoposter.get_api(cfg)
    print("Facebook Initialization Done")
    print("-------------------------")
    
    #Autoposter Initialization
    
    #Entry Initialization
    
    print("Looking for Entry....")
    entry = sheet.find_entry(data)
    print("Entry Found, number of entry is: ", entry+2)
    
    #Entry Initialization

    return data, entry, api, worksheet


