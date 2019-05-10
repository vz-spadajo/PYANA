#!/usr/bin/python3

"""Learning how to manipulate csv data"""

import csv

# get the file open, read file, loop across data ignoring row 1, move to next, return result, write out file

def main():
    totalrow = 0 # total value of a single row
    totaldict = {"date": " ", "total": 0} # tracks current highest line

    with open("2019-01-PGWU.csv", "r") as csvfile: # get file open
        csvdata = csv.reader(csvfile) # read file

        for row in csvdata: # loop across data
            if "Time" not in row[0]: # ignore first row
                for entry in range(1, len(row)): # skip first column
                    if row[entry] is "":
                        row[entry] = 0
                    totalrow = float(row[entry]) + totalrow
                if totaldict["total"] < totalrow:
                    totaldict["total"] = totalrow
                    totaldict["date"] = row[0]
                totalrow = 0
        print(totaldict)

main()