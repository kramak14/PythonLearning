import os

#This Python progam works with opening a file specified
def openfile():
    #Step 1: Give path of the file
    fileList = os.listdir(r"C:\Users\krish\prank")
    #Step 2: Print file names from directory specified
    print(fileList)

openfile()