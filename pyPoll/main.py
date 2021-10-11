# import dependencies
import os
import csv

# designate path to csv file
electionData = os.path.join("PyPoll", "Resources", "election_data.csv")

# open csv file
with open (electionData) as electFile:
    csvreader = csv.reader(electFile, delimiter=",")

    # display csv
    print (csvreader)

# the total number of votes cast


# complete list of candidates who received votes


# percentage of votes each candidate won


# total number of votes each candidate won


# winner of the election based on popular vote