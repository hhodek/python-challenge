import os
import csv

electionpath = os.path.join("Resources","election_data.csv")

cantidatevotes = {}

with open(electionpath) as electiondata:
    reader = csv.reader(electiondata)
    header = next(reader)

    for row in reader:

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
         