#https://github.com/mjohns10/csci102-week12lab.git
#Melissa Johns
#CSCI 102-Section A
#Week 12-Part A

def PrintOutput(word):
    print('OUTPUT',word)

def LoadFile(file_name):
    file = open(file_name,'r')
    lines_read = file.readlines()
    lines_read = list(map(lambda x:x.strip(),lines_read))     
    return lines_read
        
    
