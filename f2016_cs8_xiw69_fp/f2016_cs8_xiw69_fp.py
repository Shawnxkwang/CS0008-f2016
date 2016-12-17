# CS 0008
# Professor: Max Novelli
# Final project - adapted from my assignment 3 code.
# Author: Xiaokai Wang
# Email: xiw69@pitt.edu

import sys
import os
import csv

# class definition
class participants:
    # properties

    # name of the participant
    name = "nameNotFound"
    # accumulator for total distance run by the participant. float
    distance = 0
    # accumulator for the total number of runs run by the participant.
    runs = 0

    # methods

    def __init__ (self, name, d = 0):
        # set init name
        self.name = name
        # set init distance
        self.distance = d
        # set runs by this participant
        if d != 0:
            self.runs = 1

    # add single distance to the distance accumulator and increments runs by 1.
    # Argument d is a single float.
    def addDistance(self, d):
        if d > 0:
            self.distance += d
            self.runs += 1

    # add an array of distances to distance accumulator.
    # Argument ld is a list of floats.
    def addDistances(self, ld):
        for dist in ld:
            if dist > 0:
                self.distance += dist
                self.runs += 1

    # get runs
    def getRuns(self):
        return self.runs

    #get the current value of the distance accumulator.
    def getDistance(self):
        return self.distance

    # get the name of the participant of the current instance
    def getName(self):
        return self.name

    # stringify method.
    def __str__(self):
        return "Name : " + "{:>20s}".format(self.name) + \
            ". Distance run : " + "{:9.4f}".format(self.distance) + \
            ". Runs : " + "{:4d}".format(self.runs)

# key is each participant, value is an instance of class participants
participantsAndDistance = {}

# read in the master input list and get those 3 files.
def processMasterInputList():
    # total number of files
    numOfFiles = 0
    # total lines
    totalLines = 0
    # total distances
    totalDistance = 0

    fileNames = []
    try:
        # combine directories
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        # MN: why do you hard code the file name?
        filename = os.path.join(fileDir, 'f2016_cs8_fp.data/f2016_cs8_fp.data.txt')
        f = open(filename, 'r')

        #read master input list and retrieve 3 files
        for line in f:
            fileNames.append('f2016_cs8_fp.data/'+line.rstrip('\n'))
        f.close()

        # open, process and then close those 3 files
        for file in fileNames:
            numOfFiles += 1
            name = os.path.join(fileDir, file)
            fh = open(name, 'r')
            totalLines,totalDistance = processFiles(fh, totalLines, totalDistance)
            fh.close()

    except IOError:
        print("Master input list not found. \n")
    return numOfFiles, totalLines, totalDistance

# process individual file
def processFiles(fh, totalLines, totalDistance):
    # MN: DO NOT USE GLOBALS
    global participantsAndDistance

    # process each line of a single file
    for line in fh:

        if (line.split(",")[1].rstrip("\n") != 'distance'):
            totalLines += 1 # total number of lines
            if (line.split(",")[0] not in participantsAndDistance):
                # initial name
                participantsAndDistance[line.split(",")[0]] = participants(line.split(",")[0])
            # add distance
            participantsAndDistance[line.split(",")[0]].addDistance(float(line.split(",")[1].rstrip("\n")))
            # add total Distance
            totalDistance += float(line.split(",")[1].rstrip("\n"))
    return totalLines, totalDistance

def maxAndMin():
    # MN: DO NOT USE GLOBALS
    global participantsAndDistance
    # individual min {person: distance}
    minDist = {}
    # individual max {person: distance}
    maxDist = {}
    # max and min run distance
    for key in participantsAndDistance:
        isMax(maxDist, key, float(participantsAndDistance.get(key).getDistance()))
        isMin(minDist,key, float(participantsAndDistance.get(key).getDistance()))
    return maxDist,minDist

# decide max and min run
def isMax(maxDist, person, distance):
    if (len(maxDist.keys()) == 0):
        maxDist[person] = distance
    elif (distance > maxDist[next(iter(maxDist))]):
        maxDist.clear()
        maxDist[person] = distance
    else:
        return maxDist

def isMin(minDist, person, distance):
    if (len(minDist.keys()) == 0):
        minDist[person] = distance
    elif (distance < minDist[next(iter(minDist))]):
        minDist.clear()
        minDist[person] = distance
    else:
        return minDist

# sum up people with multiple records
def moreThanOnce():
    # MN: DO NOT USE GLOBALS
    global participantsAndDistance
    multipleRecords = 0
    for key in participantsAndDistance:
        if (participantsAndDistance.get(key).getRuns() > 1):
            multipleRecords += 1
    return multipleRecords
# main function
def main():
    totalParticipants = 0
    [numOfF, totalL, totalD] = processMasterInputList()
    [maxD, minD] = maxAndMin()

    #sum up total participants
    for key in participantsAndDistance:
        totalParticipants +=1
    mult = moreThanOnce()

    #print outputs
    print('\nNumber of Input files read  ' + ' : ' , numOfF)
    print('Total number of lines read  ' + ' : ' , totalL, '\n')
    print('Total distance run          ' + ' : ' , "{:.5f}".format(totalD), '\n')
    print('max distance run            ' + ' : ' , "{:.5f}".format(maxD.get(next(iter(maxD)))))
    print('  by participant            ' + ' : ' , next(iter(maxD)), '\n')
    print('min distance run            ' + ' : ' , "{:.5f}".format(minD.get(next(iter(minD)))))
    print('  by participant            ' + ' : ' , next(iter(minD)), '\n')
    print('Total number of participants ' + ': ', totalParticipants)
    print('Number of participants')
    print('with multiple records        ' + ': ', mult)

    # write to csv file
    with open('f2016_cs8_xiw69_fp.data.output.csv', 'w') as f:
        w = csv.writer(f)
        f.write('name,records,distance\n')
        for key in participantsAndDistance:
            w.writerow((key, participantsAndDistance.get(key).getRuns(), participantsAndDistance.get(key).getDistance()))

    f.close()

# main script
if __name__ == '__main__':
    main()
