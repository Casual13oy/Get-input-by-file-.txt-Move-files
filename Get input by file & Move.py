# Get input by .txt & Move files
import glob
from itertools import count
from re import X
from tkinter import N
import shutil
import os
print('""""""""""""""""""""""""""""""""""""""""""')  
# Count Wo in .txt fike line by line
with open("WO_list.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total WO that we need', count+1, 'Lines')
# Read a list in the file
for x in range(count+1):
    f = open("WO_list.txt",'r')
    search_word = f.readlines()[x][1:9]
    print('\n✔ WO', search_word)
    # print(type(search_word))
    # print(len(search_word))
    dst_folder = r"E:\pynative\reports\\"
# Look all txt files of current directory and its sub-directories
    path = r'E:\pynative\account\\'
# list to store files that contain matching word
    final_files = []             
    for file in glob.glob("{0}\**\*Pass*.json".format(path), recursive=True):
        try:
            with open(file) as fp:
                # Read the file as a string
                data = fp.read()
                if search_word in data:
                    final_files.append(file)                    
                # Extract file name from file path
                    file_name = os.path.basename(file)
                    shutil.move(file, dst_folder + file_name)                              
        except:
            print('Moved:', file_name[7:10], file_name[21:23], file_name[24:41],'slot:', file_name[53:56])
            count = count+1        
# Count amount of files
count = int(count - x)
print('\nThere are files total = ', count)
print('\nAll files have been moved successfully.')  
print('Please accept my deepest thanks\n')      
