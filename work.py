#!/usr/bin/python
print "Content-Type: text/html"
print ""

import math

def fileOpen(filename):
    inStream = open(str(filename),"r")
    Input = inStream.readlines()
    inStream.close()
    return Input

fileInfo = fileOpen("jobs.csv")

def tidyfy(listString):
    n = 0
    for string in listString:
        listString[n] = string.strip("\n")
        n += 1
    return listString

fileInfo = tidyfy(fileInfo)
print fileInfo
def specialCase(statement):
    temp = statement.split(',')
    while len(temp) > 2:
        temp[0:2] = [temp[0]+","+temp[1]]
    temp[0] = temp[0].strip("\"")
    return temp


def updateList(listString):
    newList = []
    for string in listString:
        if '"' in string:
            newList += [specialCase(string)]
        else:
            newList += [string.split(",")]
    return newList

tableList = updateList(fileInfo)
print "===="
print specialCase(fileInfo[5])
print "===="
print tableList
