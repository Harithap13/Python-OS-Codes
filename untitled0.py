
"""
Created on Thu Mar  4 10:35:39 2021

@author: harit
"""
import os
entries = os.listdir('C:/Users/harit/Desktop/series 3')
entries.sort()
for entry in entries:
    ent=entry[:-4]
    print(ent)
