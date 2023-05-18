    #Import modules
import os
import csv

    #Set election csv import path
electionpath = os.path.join("Resources","election_data.csv")

    #Creating lists
cantidatevotes = {}

    #Opening csv file with path and skipping header
with open(electionpath) as electiondata:
    reader = csv.reader(electiondata)
    header = next(reader)

        #For loop
    for row in reader:

            #Store cantidate names from column 3
        cantidatename = row[2]        

 
        if cantidatename in cantidatevotes.keys():
            cantidatevotes[cantidatename] += 1
        else:
            cantidatevotes[cantidatename] = 1
totalvote = sum(cantidatevotes.values())

for i in cantidatevotes:
    percent = round((float(cantidatevotes[i])/totalvote)*100,2)
    print(percent)

for key in cantidatevotes.keys():
    if cantidatevotes[key] == max(cantidatevotes.values()):
        winner = key

print("Election Results")
print("----------------------")
print(f"Total Votes: {totalvote}")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")
         