# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath=os.path.join('Resources','budget_data.csv')

# Control Flow (With) Statement
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []    

     
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
        total_months = str(len(month))

 # Total Revenue Sum
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))

 # Avg Revenue Change
    x = 0
    for x in range(len(revenue) - 1):
        profit_loss = int(revenue[x+1]) - int(revenue[x])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    
    monthly_change = round(Total / len(revenue_change),2)
    
# Max Increase
    profit_increase = max(revenue_change)
    y = revenue_change.index(profit_increase)
    month_increase = month[y+1]
    
# Min Decrease
    profit_decrease = min(revenue_change)
    z = revenue_change.index(profit_decrease)
    month_decrease = month[z+1]

# Analysis Output
output = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total : ${total_revenue}\n'
    f'Average Change: $ {monthly_change}\n'
    f'Greatest Increase in Profits: {month_increase} (${profit_increase})\n'
    f'Greatest Decrease in Profits: {month_decrease} (${profit_decrease})\n'
)

# Print Output Statements
print(output)

#Export .txt file
output_path = os.path.join('Analysis', "analysis.txt")

with open(output_path, "w") as txt_file:
    txt_file.write(output)