import urllib

#Reads a text file, prints out contents.
def readText():
    quoteFile = open("quotes.txt")
    fileContents = quoteFile.read()
    print(fileContents)
    quoteFile.close()
    checkCurseWords(fileContents)

#Connects to website using urllib to check if any text has curse words.
def checkCurseWords(checkText):
    #Connection to open website followed by checking text of text file
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q"+ checkText)
    output = connection.read() #Reads from the website and displays output.
    print("")
    print(output)
    connection.close() #If not used, close the connection.
    #Test for any profanity.
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("No curse words detected!")
    else:
        print("Error! Document could not be scanned.")

readText()