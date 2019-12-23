# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:30:39 2019

@author: raghav.aggiwal
"""

from load_credentials import load_credentials
from authenticate import get_vimeo_client

def get_my_channel_details():
  #load credentials
  credentials = load_credentials()
  
  #get autheticated vimeo client
  v = get_vimeo_client(**credentials)
  
  #check your channel info
  info = v.get("/me").json()
  
  print("Channel Name: ", info["name"], "\n", "Channel Link: ", info["link"], "\n")
  

#just for testing
if __name__ == "__main__":
  get_my_channel_details()