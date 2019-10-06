#hackerNoon Test Kevin

#import sys
##Debug
from collections import defaultdict


def read_file(filename):
    hostnamerq = defaultdict(int)
    with open(filename) as file:
        for line in file:
            line_list = line.split()
            hostnamerq[line_list[0]] += 1

    file = open("records_"+filename, "w")
    for host in hostnamerq:
        file.write(host+" "+str(hostnamerq[host])+"\n")
    file.close()


file_name = input('Enter file name:')
read_file(file_name)
