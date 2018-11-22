# This Python file loads the csv file and performs a filter to select the 
# readings of a particular river water level station
#
# Dataset Source: https://data.edmonton.ca/dataset/Water-Levels-and-Flows/cnsu-iagr
#
from itertools import ifilter
import csv
reader = csv.reader(open(r"Water_Levels_and_Flows.csv"),delimiter=',')
filtered = ifilter(lambda p: "North Saskatchewan River at Edmonton
" == p[2], reader)
csv.writer(open(r"Water_Levels_and_Flows2.csv",'w'),delimiter=",").writerows(filtered)
