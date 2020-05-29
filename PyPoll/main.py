# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath=os.path.join('Resources','election_data.csv')

# Define Variables
votes = []
county = []
candidates = []
khan = []
correy = []
li = []
otooley = []

# With Statement to Count Votes in CSV File
with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])


# ---------------------------
# Attempted to get unique candiate name from csv list instead of hard coding
# ---------------------------
# Python program to check if two  
# to get unique values from list 
# using numpy.unique  
# import numpy as np 
  
# # function to get unique values 
# def unique(list1): 
#     x = np.array(list1) 
#     print(np.unique(x)) 
      
# # driver code 
# list1 = [candidates] 
# unique(list1) 


    # Vote Counts per Person
    for candidate in candidates:
        if candidate == 'Khan':
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == 'Correy':
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == 'Li':
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)

# Total Vote Count
total_votes = (len(votes))
    
# Percentages to 3 Decimal Places
from decimal import Decimal

khan_percent = round(Decimal((khan_votes / total_votes) * 100), 3)
correy_percent = round(Decimal((correy_votes / total_votes) * 100), 3)
li_percent = round(Decimal((li_votes / total_votes) * 100), 3)
otooley_percent = round(Decimal((otooley_votes / total_votes) * 100), 3)

# Winner With the Highest Vote Percentage
if khan_percent > max(correy_percent, li_percent, otooley_percent):
    winner = 'Khan'
elif correy_percent > max(khan_percent, li_percent, otooley_percent):
    winner = 'Correy'  
elif li_percent > max(correy_percent, khan_percent, otooley_percent):
    winner = 'Li'
else:
    winner = "O'Tooley"

# Analysis Output
output = (
    f'Election Results\n'
    f'-------------------------\n'
    f'Total Votes: {total_votes} \n'
    f'-------------------------\n'
    f'Khan: {khan_percent}% ({khan_votes})\n'
    f'Correy: {correy_percent}% ({correy_votes})\n'
    f'Li: {li_percent}% ({li_votes})\n'
    f"O'Tooley: {otooley_percent}% ({otooley_votes})\n"
    f'-------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------')

# Print Output Statements
print(output)

# Export .txt file
output_path = os.path.join('Analysis', "analysis.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(output)



  