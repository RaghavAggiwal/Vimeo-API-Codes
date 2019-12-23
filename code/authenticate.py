# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 16:14:41 2019

@author: raghav.aggiwal
"""

#save your access token, access key and client secret in a separate json file
# it is a best practice not to hard code in script

#this script gets an authenticated service 

import vimeo

def get_vimeo_client(verbose = True, *args, **kwargs):
  try:    
    v = vimeo.VimeoClient(
        token= kwargs["access_token"],
        key= kwargs["access_key"],
        secret= kwargs["access_secret"]
    )
    
    if verbose:
      print("Successfully got an Authenticated Service")
    
    return v
  
  except Exception as e:
    print("Error Getting Authenticated Service : ", str(e))
    return None

#just for testing

#from load_credentials import load_credentials

#if __name__ == "__main__":
#    credentials = load_credentials()
#    get_vimeo_client(**credentials, verbose = False)