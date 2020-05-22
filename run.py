# run.py
# Our major logic goes here, with helpers.

import sys
import os
from pathlib import Path
import datetime
import json
import exifread

count = 0

def main():
    for arg in sys.argv[1:]:
        print("Input Directory: " + arg)
        # current_dir = Path(arg)
        printDirContents(arg)

def printDirContents(input):
    for dirpath, dirnames, files in os.walk(input):
        print('Found directory: ' + dirpath)
        for fileName in files:
            fullPath = (dirpath + '\\' + fileName)
            parseImage(fullPath)
        

def convertDate(mSecondsInput):
    d = datetime.datetime.utcfromtimestamp(mSecondsInput)
    formatedDate = d.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return formatedDate
       
def parseImage(inputFilePathStr):
    global count
    print("Image Found! " + inputFilePathStr)
    inputFile = Path(inputFilePathStr)
    with Path.open(inputFile, 'rb') as imageFile:
        workingImage = exifread.process_file(imageFile, details=False)
        for tag in workingImage.keys():
            if tag in ('EXIF DateTimeOriginal'):
                print("%s is %s" % (tag, workingImage[tag]))
                count += 1
                print("Number: " + str(count))

main()