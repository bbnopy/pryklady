def copyFile(path1,path2):
    inFile  = open(path1,’r’)
    outFile = open(path2,’w’)
    temp = inFile.read()
    outFile.write(temp)
    outFile.close()
    return
