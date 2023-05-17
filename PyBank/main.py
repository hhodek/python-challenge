import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')

netchangelist = []
netchange = 0
greatestincrease = ["", 0]
greatestdecrease = ["", 9999999999]

with open (csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_months = 1
    total_revenue = 0
    jandata = next(csvreader)
    totalmonths = total_months + 1
    totalrevenue = total_revenue + int(jandata[1])
    previousrevenue = int(jandata[1])
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        
        total_months += 1
        total_revenue += profit_loss
        netchange = int(row[1]) - previousrevenue
        previousrevenue = int(row[1])
        netchangelist = netchangelist + [netchange]
        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange
        
averagechange = round((sum(netchangelist)/len(netchangelist)), 2)
    
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {greatestincrease[0],greatestincrease[1]}")
print(f"Greatest Decrease in Profits: {greatestdecrease[0],greatestdecrease[1]}")





