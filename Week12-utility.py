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

def UpdateString(original,second,number):
    newlist = list(original)
    otherlist = []
    for i in range(len(newlist)):
        if i == number:
            otherlist.append(second)
        else:
            otherlist.append(newlist[i])
    print('OUTPUT',''.join(otherlist))

def FindWordCount(my_list,my_string):
    count = 0
    my_list = (''.join(my_list))
    my_list = my_list.split()
    print(my_list)
    for word in my_list:
        if word == my_string:
            count +=1
    return count

def ScoreFinder(list1,list2,my_string):
    if my_string in list1:
        place = list1.index(my_string)
        score = list2[place]
        print('OUTPUT',my_string,'got a score of',score)
    else:
        print('OUTPUT Player not found')
        
    
