#!/usr/bin/python

import math
import random

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
tableList.pop(0)
tableList.pop()
tableList.pop()


def secondlist(listString):
    newList = []
    for list in listString:
        newList.append(int(float(list[1])*10))
    return newList

def secondlistname(listString):
    newList = []
    for list in listString:
        newList.append(list[0])
    return newList
probs =  secondlist(tableList)
names = secondlistname(tableList)

def choose(probs,names):
    newList = []
    count = 0
    while count < len(probs):
        newList.extend([names[count]] * probs[count])
        count += 1
    return random.choice(newList)

def randomJob():
    print choose(probs,names)
def breakdown():
    jobs = {}
    count = 0
    while count < len(names):
        jobs.update({names[count]:0})
        count += 1
    for x in range(0,100000):
        jobs[choose(probs,names)] += 1
    print "For 100000 jobs, this is the amount of people that will have that job"
    print jobs
    
print "Type randomJob() to get a random job, and type breakdown() to get a breakdown"




    
