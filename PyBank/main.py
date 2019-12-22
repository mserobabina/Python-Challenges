# defining dependencies
import os
import csv

#path to collect data
csvpath = os.path.join("Resources",'budget_data.csv')

#variabes
total_months = []
total_profit = []
monthly_profit_change = []

#read in csv file
with open(csvpath,newline="", encoding='utf-8') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  header = next(csvreader)
  for row in csvreader:
      total_months.append(row[0])
      total_profit.append(int(row[1]))
         
#loop through the data  
for i in range(len(total_profit)-1):
    monthly_profit_change.append(total_profit[i+1]-total_profit[i])
    
max_increase_value=max(monthly_profit_change)
max_decrease_value=min(monthly_profit_change)
max_increase_month = monthly_profit_change.index(max(monthly_profit_change))+1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change))+1

#print financial analysis
print("Financial Analysis")
print("------------------------------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total:${sum(total_profit)}")
print(f"Average Change:{round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits:{total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits:{total_months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = os.path.join("Resources",'budget_analysiscmd.txt')
#read in csv
with open(output_file,"w") as file:
    file.write(f"Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months:{len(total_months)}")
    file.write("\n")
    file.write(f"Total:${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change:{round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
    file.write("\n")
    
    
     