import os

#This Python progam works with opening a file specified
def renamefile():
    #Step 1: Give path of the file
    fileList = os.listdir(r"C:\Users\krish\prank")
    actualPath = os.getcwd()
    print("Current working directory is: " + actualPath)
    os.chdir(r"C:\Users\krish\prank")
    #Step 3: Loop through each file, renaming the file
    for fileName in fileList:
        os.rename(fileName, fileName.translate(None,"0123456789"))
        os.chdir(actualPath)

renamefile()