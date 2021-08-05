#!/usr/bin/env python
# coding: utf-8

# In[58]:


import os
import glob 


# In[30]:


dirpath = "/Users/dwightsablan/Desktop/turtle_detection/data"


# In[31]:


#text files
text_files = [f for f in os.listdir(dirpath) if f.endswith('.TXT')]
#image files
image_files = [f for f in os.listdir(dirpath) if f.endswith('.JPG')]


# In[43]:


# new directories
images_dir = "images"
labels_dir = "labels"

# Parent Directory paths
parent_dir = "/Users/dwightsablan/Desktop/turtle_detection/data"
  
# Paths
path = os.path.join(parent_dir, image_dir)
path_2 = os.path.join(parent_dir, labels_dir)


# In[44]:


# Create new directories
os.mkdir(path)
os.mkdir(path_2)


# In[48]:


# Move image files to image directory
for file in image_files:
    os.rename(parent_dir + "/" + file, path + "/" + file)


# In[49]:


# Move text files to text directory
for file in text_files:
    os.rename(parent_dir + "/" + file, path_2 + "/" + file)


# In[170]:


def find_decimal(test_str):
    index_list = [i for i, ltr in enumerate(test_str) if ltr == '.']
    return index_list[-1]


# In[191]:


def process_text_files(dir_filepath):
    text_file_paths = glob.glob(dir_filepath + "/*") 
    
    #For each file in the directory, fix the format
    for filepath in text_file_paths:
        file = open(filepath, 'r')
        data = file.readlines()
        for i, line in enumerate(data):
            index = find_decimal(line)
            data[i] = line[:index-1] + ' ' + line[index-1:]
        file = open(filepath, 'w')
        file.writelines(data)
            
        file.close()


# In[192]:


process_text_files(path_2)

