def writeSampleValue():
    f = pickAFile() # File where the original sound resides
    source = makeSound(f)
    eol = chr(11)
    getPath = f.split(’.’) # find the ’.’ in the full file name
    suffix = ’.txt’
    myFile = getPath[0] + suffix # get the part leading up to the ’.’ and make it  a ".txt" file
    outFile = open(myFile,’w’)
    endCurrentSound = getLength(source)

    for pos in range (1, endCurrentSound + 1):
        sampVal =  getSampleValueAt(source,pos)
        stringVal = ’
        outFile.write(stringVal + eol) # outFile.write(eol)
    outFile.close()
