#BW plan
def main():

    #open the existing data.txt file as input file
    inputFile = open ("TrialBW22.txt","r")
    outputFile = open("BW1.csv","w")
 
#   listName = inputFile.readlines())
    
   # read one line from inputFile
   #and write the line to outputFile
    #print(lengthWord)
    '''
    OLD METHOD !!!!!!!!!
    
    count = 0
    
    for count in range(len(listName)):
            lineRead = listName[count]
 #           v =lengthWord.append(lineRead)
            print(lineRead.strip("\n\r"))
##  Very important, please note that you use strip("\n\r") print(lineRead.strip("\n\r"))
            outputFile.write(lineRead)
            count+=1
    '''
##    print(inputFile.read(10));;;  Test Trial To see if it reads it
    for line in inputFile:
        #print(line.strip("\n\r"))
        outputFile.write(line)
        

    #Append a line of text to outputFile
    outputFile.write("Computer Programing is exciting:\n")
    inputFile.close()
    outputFile.close()
## CHECK THE STATUS MODE,CLOSURE AND LOCATION OF FILE
    print("Mode: "+inputFile.mode)
    print("is closed: "+str(inputFile.closed))
    print("File Name: "+inputFile.name)

    print("Mode: "+outputFile.mode)
    print("is closed: "+str(outputFile.closed))
    print("File Name: "+outputFile.name)
        
main()

