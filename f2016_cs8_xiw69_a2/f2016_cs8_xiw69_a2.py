
# Xiaokai Wang
# xiw69@pitt.edu
# CS 0008  -f2016
# assignmnet #2

import os
import csv

# global vars lines -> total lines counter, distances -> total distance counter
#------------------------------------------------------------------------------
lines = 0
distances =0
partial_line = "Partial Total # of lines"
partial_distance = "Partial distance run"
final_line = "Total # of lines"
final_distance = "Total distance run"
#------------------------------------------------------------------------------

# processFile function, read and count single file's lines and distances
def processFile(fh):
    number_of_lines = 0
    total_distance = 0
    for line in fh:
        number_of_lines+=1
        total_distance += float(line.split(",")[1].rstrip("\n"))
    global lines
    global distances
    lines += number_of_lines
    distances += total_distance
    #print(total_distance, number_of_lines);
    return number_of_lines, total_distance


# printKV function, print key-value pairs for single file's lines and distances
def printKV(key, value, klen = 0):
    key_len = len(key)
    real_len = max(key_len,klen)
    p_key = "{:<{real_l}}".format(key, real_l=real_len)
    p_value = 0
    if isinstance(value, str):
        p_value = "{:<20}".format(value)
    elif isinstance(value, float):
        p_value = "{:10.3f}".format(value)
    elif isinstance(value, int):
        p_value = "{:10}".format(value)
    else:
        p_value = "{:15}".format(value)

    print_key_value = p_key +" : " +p_value
    print(print_key_value)



# main script
def main(f_name):
    # read in file

    # try open and process file
    try:
        f = open(f_name, 'r')
        t_lines, t_distance = processFile(f)
        printKV("File read", f_name, 25)
        printKV(partial_line, t_lines,25)
        printKV(partial_distance, t_distance, 25)
        print("\n");
        f.close()
    except IOError:
        print("this file does not exist or you entered wrong file name, please try again.\n");



if __name__ == '__main__':
    # infinite loop to continuously read in files
    while True:
        f_name = input("Please provide the file name : ")
        print("\n")
        quit = f_name.lower()
        if ( quit == '' or quit =='quit' or quit =='q'):
            printKV("File to be read", "quit", 25)
            printKV(final_line, lines, 25)
            printKV(final_distance, distances, 25)
            break
        else:
            main(f_name)





