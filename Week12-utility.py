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
    for word in my_list:
        if word == my_string:
            count +=1
    return count

def ScoreFinder(list1,list2,my_string):
    word1 = my_string.capitalize()
    word2 = my_string.lower()
    if word1 in list1:
        place = list1.index(word1)
        score = list2[place]
        print('OUTPUT',my_string,'got a score of',score)
    elif word2 in list1:
        place = list1.index(word2)
        score = list2[place]
        print('OUTPUT',my_string,'got a score of',score)
    else:
        print('OUTPUT Player not found')

def Union(list1,list2):
    newlist = list1 + list2
    return newlist

def Intersection(list1,list2):
    newlist = []
    for word in list1:
        if word in list2:
            newlist.append(word)
    return newlist

def NotIn(list1,list2):
    newlist = []
    for word in list1:
        if word not in list2:
            newlist.append(word)
    return newlist

