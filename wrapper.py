#!/usr/bin/python3

import sheet
import fb_autoposter
import pandas
import time
import decryptor

def initialize():
    gc = sheet.gacc_init()
    sheet.list_available(gc)
    print('-------------------------')    
    try:#Tries to get page id  and fb api key from the google sheet
        token_encrypted,page_id,spreadsheet = sheet.get_settings(gc)
        key = decryptor.decrypt(token_encrypted)
    except:# if it fails ask user to provide it instead
        print("Couldn't read api key.")
        key = input("Input your facebook user access api key: ")
        print("Couldn't read page id.")
        page_id = input("Please specify page id: ")   
    data, worksheet = sheet.create_frame(gc ,spreadsheet)
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

    return data, entry, api, worksheet, max_entry


