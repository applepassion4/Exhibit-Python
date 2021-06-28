#module for reading csv files

import os
import csv

# Set path for files
csvpath = os.path.join('Resources','budget_data.csv')

#Declare variables
total_months = []
total_profits = []
profit_changes= 0
monthly_changes=[]
previous_value =0

# Open the CSV File
with open(csvpath) as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    #Had to skip the the header or otherwise will count it as another month
    csv_reader= next(csvreader)

    for row in csvreader:

# Total of months & profits/losses
       total_months.append(row[0])
       total_profits.append(row[1])
       
    #print(len(total_months))

#The net total amount of "Profit/Losses" over the entire period

    total_profits=[int(x) for x in total_profits] 
    total_profits_sum=sum(total_profits) 
    #print (total_profits_sum)

#Changes in "Profit/Losses" over the entire period
for i in range(len(total_profits)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_changes.append(total_profits[i+1]-total_profits[i])
        average_changes = sum(monthly_changes) / len(total_months)
    
max_increase_value = max(monthly_changes)
max_decrease_value = min(monthly_changes)

max_increase_month = monthly_changes.index(max(monthly_changes)) + 1
max_decrease_month = monthly_changes.index(min(monthly_changes)) + 1 


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total Profits: ${sum(total_profits)}")
print(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = os.path.join("Analysis", "output.txt")

with open(output_file,"w") as txt_file:
    

# Write methods to print to Financial_Analysis_Summary 
    txt_file.write("Final Output")
    txt_file.write("\n")
    txt_file.write("----------------------------")
    txt_file.write("\n")
    txt_file.write(f"Total Months: {len(total_months)}")
    txt_file.write("\n")
    txt_file.write(f"Total: ${sum(total_profits)}")
    txt_file.write("\n")
    txt_file.write(f"Average Change: {round(sum(monthly_changes)/len(monthly_changes),2)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
