# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:29:33 2019

@author: raghav.aggiwal
"""

#Load credentials from config file
#this will run by default as soon as you run any script

import json
import os

def load_credentials(*args, **kwargs):
  #path to your config file
  vimeo_config_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ),\
                                                         '..','config files', \
                                                         'vimeo_config_english.json'))
  
  try:
    with open(vimeo_config_file) as f:
      access_credential = json.load(f)
        
      access_token = access_credential['access_token']
      access_key = access_credential['access_key']
      access_secret = access_credential['access_secret']
      
      f.close()
      
      print("Credentials Loaded Successfully!")
      
      credentials = {"access_token" : access_token, 
                     "access_key" : access_key,
                     "access_secret" : access_secret}
      
      return credentials
    
  except Exception as e:
    print("Error importing credentials from config file : ", str(e))
    
#if __name__ == "__main__":
#  credentials = load_credentials()
#  print(credentials["access_token"])