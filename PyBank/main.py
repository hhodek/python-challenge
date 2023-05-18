    #Importing modules os and csv
import os
import csv

    #Setting import path for csv files
csvpath = os.path.join( 'Resources', 'budget_data.csv')

    #Creating lists to store data and initialized net change variable
netchangelist = []
netchange = 0
greatestincrease = ["", 0]
greatestdecrease = ["", 9999999999]

    #Opening csv file with path variable and skipping header
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

        #Initiliazing and setting variables
    total_months = 1
    total_revenue = 0
    jandata = next(csvreader)
    totalmonths = total_months + 1
    totalrevenue = total_revenue + int(jandata[1])
    previousrevenue = int(jandata[1])

        #For loop
    for row in csvreader:
        
            #Storing column data seperately
        date = row[0]
        profit_loss = int(row[1])
        
            #For each month in date column add a value of 1 to total_months count
        total_months += 1
        
            #For each amount in profit/loss column add to total revenue count
        total_revenue += profit_loss

            #Calculate and store changes over whole period
        netchange = int(row[1]) - previousrevenue
        previousrevenue = int(row[1])
        netchangelist = netchangelist + [netchange]

            #Find and store greatest increase in profits and the date
        if netchange > greatestincrease[1]:
            greatestincrease[0] = row[0]
            greatestincrease[1] = netchange
            #Find and store greatest decrease in profits and the date
        if netchange < greatestdecrease[1]:
            greatestdecrease[0] = row[0]
            greatestdecrease[1] = netchange
        
    #Calculating and formatting average change       
averagechange = round((sum(netchangelist)/len(netchangelist)), 2)

    #Increase/Decrease in profits variables
increasedate = greatestincrease[0]
increaseamount = greatestincrease[1]
decreasedate = greatestdecrease[0]
decreaseamount = greatestdecrease[1]

    
    #Printing results to terminal
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {increasedate} (${increaseamount})")
print(f"Greatest Decrease in Profits: {decreasedate} (${decreaseamount})")

    #Setting output path
outputpath = os.path.join( 'analysis' , 'FinancialAnalysisResults.txt')

    #Writing results as a txtfile in analysis folder
with open(outputpath, 'w') as txtfile:
     txtfile.write('\n'"Financial Analysis"'\n')
     txtfile.write('\n'"-----------------------"'\n')
     txtfile.write(f"\nTotal Months: {total_months}\n")
     txtfile.write(f"\nTotal: ${total_revenue}\n")
     txtfile.write(f"\nAverage Change: ${averagechange}\n")
     txtfile.write(f"\nGreatest Increase in Profits: {increasedate} (${increaseamount})\n")
     txtfile.write(f"\nGreatest Decrease in Profits: {decreasedate} (${decreaseamount})\n")






