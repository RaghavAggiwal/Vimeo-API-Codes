# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 18:01:30 2019

@author: raghav.aggiwal
"""



import os
from authenticate import get_vimeo_client
from load_credentials import load_credentials
from pandas import  read_excel



credentials = load_credentials()

#this function updates thumbnail image for a video uri
def update_thumbnail_image(verbose = True, *args, **kwargs):
  v = get_vimeo_client(**credentials)
  
  try:
    video_uri = kwargs['video_uri']
    thumbnail_path = kwargs['thumbnail_path']
    
    v.upload_picture(video_uri, 
                     thumbnail_path, 
                     activate = True)
    print("Thumbnail updated successfully for video uri : ", video_uri, "\n")
    
  except Exception as e:
    print("Error updating thumbnail for video uri: ", video_uri, "\nError : ", str(e), "\n")
    
    return False
  
  return True
  
def update_video_info(verbose = True, *args, **kwargs):
  v = get_vimeo_client(**credentials)
  
  try:
    video_uri = kwargs['video_uri']
    tags = kwargs['tags']
    description = kwargs['description']
    title = kwargs['title']
    
    v.patch(video_uri, 
            data = {'name' : title,
                    'description' : description,
                    'tags' : tags}
      )
    
    print("Video Info updated successfully for video uri : ", video_uri, "\n")
    
  except Exception as e:
    print("Error updating video info for video uri: ", video_uri, "\nError : ", str(e), "\n")
    
    return False
  
  return True
  

if __name__ == "__main__":
  #update data is present in a separate excel, reading from the file
  update_file = r"D:/vimeo/Codes/update_english.xlsx"
  update_data = read_excel(update_file)
  update_data.astype('str').dtypes
  
  cnt = 0
  
  for i, row in update_data.iterrows():
    video_uri = update_data.loc[i, "uri"]
    title = update_data.loc[i, "title"]
    description = update_data.loc[i, "description"]
    tags = update_data.loc[i, "tags"]
    
    update_dict = {"video_uri" : video_uri, 
                   "title" : title,
                   "description" : description,
                   "tags" : tags
                   }
    
    flag = update_video_info(**update_dict)
    
    if flag is True:
      update_data.loc[i, "update_message"] = "Done"
      cnt = cnt + 1
    else:
      update_data.loc[i, "update_message"] = "Not Done"
        
    
    
    if(cnt % 100 == 0):
      print("Done : ", cnt)
      
  print("Done : ", cnt)
  
  #write results to output file
  output_file_name = 'channnel_info_update'
  output_file = os.path.abspath(os.path.join(os.path.dirname( __file__ ),\
                                                        '..','results', \
                                                         output_file_name))
  update_data.to_excel(output_file)

  print("Info saved to file : ", output_file)
  