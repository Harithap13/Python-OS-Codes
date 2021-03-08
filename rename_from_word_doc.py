# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:42:30 2021

@author: harit
"""
#make sure you have installed the docx using pip
#pip install python-docx 
# This particular code is to rename images from the word document when given in a particular order.

import docx
import os
l=[]
doc = docx.Document("Path to the word document")
all_paras = doc.paragraphs
for para in all_paras:
    l.append(para.text)

n=1
v=[]
dic={} # here we need a particular file name assigned to number 1,2,3 etc. Assign any iterable value as required.
for y in l:
    dic[y+'.jpg']=str(n) # use .jpg for images or change to required file type
    v.append(str(n))
    n=n+1

path = 'Path to the folder containing the images'
files = os.listdir(path)
os.chdir('Path to the folder containing the images')
for file in files:
    print(file,dic[file]) #For generating a list of File name and index pairs 
    v.remove(dic[file]) # used to find which items listed in word doc are not available in the file repository
    os.rename(file, 'test_image'+dic[file]+'.jpg') # use .jpg for images or change to required file type