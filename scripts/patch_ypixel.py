#!/usr/bin/python
import sys
import h5py

data = sys.stdin.readlines()
for files in data:
    #open the file
    theFile = files.rstrip('\n')
    fileHandle = h5py.File(theFile, 'r+')
    if not fileHandle:
        print ('couldnt open ', theFile)
        continue
         
    print ('up to: ', theFile)
    '''     
    theDataSet = fileHandle['entry1/instrument/parameters/y_pixels_per_mm']
    theDataSet[::] = 0.33     
    '''

    #when you are finished close the file
    if fileHandle:
        fileHandle.close()
    
