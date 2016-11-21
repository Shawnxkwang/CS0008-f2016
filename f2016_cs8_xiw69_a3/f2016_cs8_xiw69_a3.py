"""
assignment 3
Xiaokai Wang
xiw69@pitt.edu

"""
import sys
import os
import csv

# global vars
#-------------------------------
minDist = {}  # individual min {person: distance}
maxDist = {}  # individual max {person: distance}
numOfFiles = 0  # total number of files
totalLines = 0  # total lines
totalDistance = 0 # total distances
totalParticipants = 0 # total participants
multipleRecords = 0 # multiple records number of people
participantsAndDistance = {} # key is each participant, value is an array[0.total distance, 1.appear times]
#-------------------------------

# read in the master input list and get those 3 files.
def processMasterInputList():
    global numOfFiles
    fileNames = []
    try:
        # combine directories
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'f2016_cs8_a3.data/f2016_cs8_a3.data.txt')
        f = open(filename, 'r')

        #read master input list and retrieve 3 files
        for line in f:
            fileNames.append('f2016_cs8_a3.data/'+line.rstrip('\n'))
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
    global totalLines, totalDistance, participantsAndDistance, minDist, maxDist

    # process each line of a single file
    for line in fh:
        totalLines +=1 # if count the header, we have three more lines

        if (line.split(",")[1].rstrip("\n") != 'distance'):

            if (line.split(",")[0] not in participantsAndDistance):
                values = []
                values.append(float(line.split(",")[1].rstrip("\n")))
                values.append(1)
                participantsAndDistance[line.split(",")[0]] = values

                # decide max and min run disance
                isMax(line.split(",")[0], float(line.split(",")[1].rstrip("\n")))
                isMin(line.split(",")[0], float(line.split(",")[1].rstrip("\n")))

            elif (line.split(",")[0] in participantsAndDistance):
                # add appear times
                times = participantsAndDistance.get(line.split(",")[0])[1]
                times += 1
                participantsAndDistance[line.split(",")[0]][1] = times

                # sum up distance
                dist = participantsAndDistance.get(line.split(",")[0])[0]
                dist += float(line.split(",")[1].rstrip("\n"))
                participantsAndDistance[line.split(",")[0]][0] = dist

                # max and min run distance
                isMax(line.split(",")[0], float(line.split(",")[1].rstrip("\n")))
                isMin(line.split(",")[0], float(line.split(",")[1].rstrip("\n")))

            totalDistance += float(line.split(",")[1].rstrip("\n")) # add total Distance


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
        if (participantsAndDistance.get(key)[1] > 1):
            multipleRecords += 1

# main function
def main():
    global totalParticipants
    processMasterInputList()

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
    with open('f2016_cs8_xiw69_a3.data.output.csv', 'w') as f:
        w = csv.writer(f)
        for key in participantsAndDistance:
            w.writerow((key, participantsAndDistance.get(key)[1], participantsAndDistance.get(key)[0]))

    f.close()

# main script
if __name__ == '__main__':
    main()