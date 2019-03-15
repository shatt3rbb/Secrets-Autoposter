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
    try:#Tries to get fb api key and page id from the settings file
        lines = [] 
        f = open("settings.midget","r+") #open for read/write
        for line in f:lines.append(line)
        f.close()
        key = lines[1].replace("fb_token = '", "")
        key = key.replace("'", "")
        key = key.replace("\n", "")
        page_id = lines[2].replace("page_id = '", "")
        page_id = page_id.replace("'", "")
        page_id = page_id.replace("\n", "")
    except:# if it fails ask user to provide it instead
        print("Couldn't read api key from settings file.")
        key = input("Input your facebook user access api key: ")
        print("Couldn't read page id from settings file.")
        page_id = input("Please specify page id: ")   
    
    #Autoposter initialization
    
    print("Initializing facebook poster... Please wait....")
    cfg = fb_autoposter.init_token(key,page_id)
    api = fb_autoposter.get_api(cfg)
    print("Facebook Initialization Done")
    print("-------------------------")
    
    #Autoposter Initialization
    
    #Entry Initialization
    
    print("Looking for Entry....")
    entry = sheet.find_entry(data)
    print("Entry Found, number of entry is: ", entry+2)
    max_entry = sheet.find_empty_cell(data)
    print("Post left to do: " + str(max_entry - (entry+2)))
    #Entry Initialization

    return data, entry, api, worksheet


