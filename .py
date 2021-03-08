
"""
Created on Thu Mar  4 10:35:39 2021

@author: harit
"""
# Code to list all the files in a directory without the extensions.
import os
entries = os.listdir('C:/Users/path to directory')
entries.sort()
for entry in entries:
    ent=entry[:-4]
    print(ent)
