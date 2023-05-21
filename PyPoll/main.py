    #Import modules
import os
import csv

    #Set election csv import path
electionpath = os.path.join("Resources","election_data.csv")

    #Creating dictionaries
candidatevotes = {}

    #Opening csv file with path and skipping header
with open(electionpath) as electiondata:
    reader = csv.reader(electiondata)
    header = next(reader)

        #For loop
    for row in reader:

            #Store cantidate names from column 3
        candidatename = row[2]        

 
        if candidatename in candidatevotes.keys():
            candidatevotes[candidatename] += 1
        else:
            candidatevotes[candidatename] = 1
totalvote = sum(candidatevotes.values())

for candidate, votes in candidatevotes.items():
    percent = round((votes/totalvote)*100,2)


for key in candidatevotes.keys():
    if candidatevotes[key] == max(candidatevotes.values()):
        winner = key


    #Printing results to terminal
print("Election Results")
print("----------------------")
print(f"Total Votes: {totalvote}")
print("----------------------")
for candidate, votes in candidatevotes.items():
    percent = round((votes/totalvote)*100,3)
    print(f"{candidate}: {percent}% ({votes})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

    #Set outputpath
outputpath = os.path.join('analysis' , 'ElectionResults.txt')

    #Writing results as textfile to analysis folder
with open(outputpath, 'w') as txtfile:
    txtfile.write('\n'"Election Results"'\n')
    txtfile.write('\n'"----------------------"'\n')
    txtfile.write(f"\nTotal Votes: {totalvote}\n")
    txtfile.write('\n'"----------------------"'\n')
    for candidate, votes in candidatevotes.items():
        percent = round((votes/totalvote)*100,3)
        txtfile.write(f"\n{candidate}: {percent}% ({votes})\n")
    txtfile.write("\n----------------------\n")
    txtfile.write(f"\nWinner: {winner}\n")
    txtfile.write('\n'"----------------------"'\n')