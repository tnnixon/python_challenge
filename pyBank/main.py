#import dependencies
import os
import csv

#set variables to zero
totalMos = 0
totalNet = 0
prevChange = 0
netChangeList = []

#path to csv file
budgetData = os.path.join("PyBank", "Resources", "budget_data.csv")

#open csv file
with open (budgetData) as budgetFile:
    csvreader = csv.reader(budgetFile, delimiter=",")

#display csv
    #print (csvreader)

#extract header data
    header = next(csvreader)
#extract january data
    janData = next(csvreader)

    totalMos = totalMos + 1
    totalNet = totalNet + int(janData[1])
    prevChange = int(janData[1])
    months = []

#loop through rows in csv
    for row in csvreader:
        #print(row)

    # The total number of months included in the dataset
        months.append(row[0])
        totalMos = totalMos + 1
        totalNet = totalNet + int(row[1])
      
    # The net total amount of "Profit/Losses" over the entire period
        netChange =  (int(row[1]) - prevChange)

    # append net change to list
        #print (netChange)
        prevChange = int(row[1])
        netChangeList.append(netChange)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    netAvgChange = sum(netChangeList) / len(netChangeList)

# The greatest increase in profits (date and amount) over the entire period
    maxValue = max(netChangeList)
    greatMonth = netChangeList.index(maxValue)

# The greatest decrease in profits (date and amount) over the entire period
    minValue = min(netChangeList)
    minMonth = netChangeList.index(minValue)

# print analysis results to terminal
    print ("Financial Analysis")
    print ("----------------------------")
    finAnalysis = [
        "Total Months: " + str(totalMos),
        "Total: $" + str(totalNet),
        "Average Change: $" + str(netAvgChange),
        "Greatest Increase in Profits: " + str(months[greatMonth]) + " " + "($" + str(maxValue) + ")",
        "Greatest Decrease in Profits: " + str(months[minMonth]) + " " + "($" + str(minValue) + ")"
        ]
for results in finAnalysis:
    print(results)

header = ['Financial Analysis']
dash = ['----------------------------']
data = [
        ["Total Months: " + str(totalMos)],
        ["Total: $" + str(totalNet)],
        ["Average Change: $" + str(netAvgChange)],
        ["Greatest Increase in Profits: " + str(months[greatMonth]) + " " + "($" + str(maxValue) + ")"],
        ["Greatest Decrease in Profits: " + str(months[minMonth]) + " " + "($" + str(minValue) + ")"]
        ]

#specify path to write to and output file name
output_path = os.path.join("PyBank", "Resources", "financial_analysis.csv")
output_file = os.path.join("financial_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as output_file:

    # Initialize csv writer
    writer = csv.writer(output_file)
    writer.writerows([header])
    writer.writerows([dash])
    writer.writerows(data)