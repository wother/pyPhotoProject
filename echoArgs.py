# echoArgs.py
import sys
import os
from pathlib import Path
import datetime
import json
import exifread

def main():
    for arg in sys.argv[1:]:
        print("Input Directory: " + arg)
        current_dir = Path(arg)
        printDirContents(current_dir)

def printDirContents(input):
    
    for entry in input.iterdir():
        # entry is a pathlib.WindowsPath object
        print(entry.name)
        # if the path points at an Image parse it.
        winPathString = str(entry.name)
        # else if it is a directory crawl into it.
        if winPathString.endswith('.JPG') or winPathString.endswith('.NEF'):
            parseImage(entry)
        

def convertDate(mSecondsInput):
    d = datetime.datetime.utcfromtimestamp(mSecondsInput)
    formated_date = d.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    return formated_date

def returnJSONDateStamp (timeStampInput):
    return json.dumps(timeStampInput)
       
def parseImage(winPathInput):
    with Path.open(winPathInput, 'rb') as imageFile:
        workingImage = exifread.process_file(imageFile, details=False)
        for tag in workingImage.keys():
            if tag in ('EXIF DateTimeOriginal'):
                print("%s is %s" % (tag, workingImage[tag]))

main()