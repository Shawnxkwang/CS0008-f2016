
# final project - adapted from my assignment 3 code.
# Xiaokai Wang
# xiw69@pitt.edu

import sys
import os
import csv

# global vars
#-------------------------------
# individual min {person: distance}
minDist = {}
# individual max {person: distance}
maxDist = {}
# total number of files
numOfFiles = 0
# total lines
totalLines = 0
# total distances
totalDistance = 0
# total participants
totalParticipants = 0
# multiple records number of people
multipleRecords = 0
# key is each participant, value is an instance of class participants
participantsAndDistance = {}
#-------------------------------

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

# read in the master input list and get those 3 files.
def processMasterInputList():
    global numOfFiles
    fileNames = []
    try:
        # combine directories
        fileDir = os.path.dirname(os.path.realpath('__file__'))
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
            processFiles(fh)
            fh.close()

    except IOError:
        print("Master input list not found. \n")


# process individual file
def processFiles(fh):
    global totalLines, totalDistance, participantsAndDistance

    # process each line of a single file
    for line in fh:

        if (line.split(",")[1].rstrip("\n") != 'distance'):
            totalLines += 1 # total number of lines
            if (line.split(",")[0] not in participantsAndDistance):
                # initial name
                participantsAndDistance[line.split(",")[0]] = participants(line.split(",")[0])
            # add distance
            participantsAndDistance[line.split(",")[0]].addDistance(float(line.split(",")[1].rstrip("\n")))

            totalDistance += float(line.split(",")[1].rstrip("\n")) # add total Distance

def maxAndMin():
    global participantsAndDistance
    # max and min run distance
    for key in participantsAndDistance:
        isMax(key, float(participantsAndDistance.get(key).getDistance()))
        isMin(key, float(participantsAndDistance.get(key).getDistance()))

# decide max and min run
def isMax(person, distance):
    if (len(maxDist.keys()) == 0):
        maxDist[person] = distance
    elif (distance > maxDist[next(iter(maxDist))]):
        maxDist.clear()
        maxDist[person] = distance
    else:
        return maxDist

def isMin(person, distance):
    if (len(minDist.keys()) == 0):
        minDist[person] = distance
    elif (distance < minDist[next(iter(minDist))]):
        minDist.clear()
        minDist[person] = distance
    else:
        return minDist

# sum up people with multiple records
def moreThanOnce():
    global participantsAndDistance, multipleRecords
    for key in participantsAndDistance:
        if (participantsAndDistance.get(key).getRuns() > 1):
            multipleRecords += 1

# main function
def main():
    global totalParticipants
    processMasterInputList()
    maxAndMin()
    #sum up total participants
    for key in participantsAndDistance:
        totalParticipants +=1
    moreThanOnce()

    #print outputs
    print('\nNumber of Input files read  ' + ' : ' , numOfFiles)
    print('Total number of lines read  ' + ' : ' , totalLines, '\n')
    print('Total distance run          ' + ' : ' , "{:.5f}".format(totalDistance), '\n')
    print('max distance run            ' + ' : ' , "{:.5f}".format(maxDist.get(next(iter(maxDist)))))
    print('  by participant            ' + ' : ' , next(iter(maxDist)), '\n')
    print('min distance run            ' + ' : ' , "{:.5f}".format(minDist.get(next(iter(minDist)))))
    print('  by participant            ' + ' : ' , next(iter(minDist)), '\n')
    print('Total number of participants ' + ': ', totalParticipants)
    print('Number of participants')
    print('with multiple records        ' + ': ', multipleRecords)

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