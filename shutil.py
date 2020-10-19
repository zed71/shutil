import shutil
import os

#set where the source files are
source = 'C:/Users/Brandon/Desktop/Folder A'

#set the destination path to folder B
destination = 'C:/Users/Brandon/Desktop/Folder B'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i,destination)
