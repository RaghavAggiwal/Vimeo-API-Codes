# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 17:03:33 2019

@author: raghav.aggiwal
"""

import os
from authenticate import get_vimeo_client
from load_credentials import load_credentials
from pandas import DataFrame
from math import ceil



#this function get list of videos on Vimeo channel
def get_channel_list():
  
  #load credentials which can be reused again and again to get vimeo client
  credentials = load_credentials()
  
  v = get_vimeo_client(**credentials)
  
  video_list = v.get('https://api.vimeo.com/me/videos?fields=uri,name&page=1&per_page=100&sort=date&direction=desc').json()
  
  total_videos = video_list['total']
  per_page = video_list['per_page']
  
  last_page = ceil(total_videos/per_page)
  
  print("Total Videos on Vimeo: ", total_videos, "\nPer page results: ", per_page, "\nLast Page to be iterated: ", last_page, "\n\n")
  
  
  #Iterate over all videos and store the meta data in a dataframe
  cnt = 0 
  
  result = DataFrame({"uri": [], "name":[]})
  
  for page_number in range(1,last_page+1):
    api_get_request = ('https://api.vimeo.com/me/videos?fields=uri,name&page={0}&per_page=100&sort=date&direction=desc').format(page_number)
      
    v = get_vimeo_client(**credentials, verbose = False)
  
    video_list = v.get(api_get_request).json()
      
    for v in video_list['data']:
      result.loc[cnt, "uri"] = v['uri']
      result.loc[cnt, "name"] = v['name']
          
      cnt = cnt + 1
          
      if(cnt % 100 == 0):
        print("Done: ", cnt)
  
  print("Done: ", cnt)
  
  return result
  

if __name__ == "__main__":
  result = get_channel_list()
  
  output_file_name = 'channel_list.xlsx'
  output_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ),\
                                                        '..','results', \
                                                         output_file_name))
  result.to_excel(output_file)

  print("Channel videos info saved to file : ", output_file)
  