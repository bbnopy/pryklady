def copyFile(path1,path2):
    inFile = open(path1,’rb’)
    outFile = open(path2,’wb’)
    more = 1 # set so we can perform the first read

    while (more > 0 ):
        # Alternative (less readable but cooler): while(more):
        temp = inFile.read(4096) # reads 4096 bytes or whatever is left at end
        more = len(temp) # when no more data more is set to 0
        outFile.write(temp)
        outFile.close()
    return
