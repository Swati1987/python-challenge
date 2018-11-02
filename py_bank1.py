import os
import csv
from statistics import mean

csvpath = os.path.join("budget_data.csv") 
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    dates = []
    revenues = []

    for row in csvlist:
        dates.append(row[0])
        revenues.append(int(row[1]))
    
    revchange = []
    revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    max_change = max(revchange)
    biggest_loss = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    max_month = None
    loss_month = None
    initial_val = None
    
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == biggest_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])
    
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months : {total_month}\n"
    f"Average Change : ${avg_change}\n"
    f"Greatest Increase in Revenue: {max_month} (${max_change})\n"
    f"Greatest Decrease in Revenue: {loss_month} (${biggest_loss})\n")    
    
print(output)

with open("newbudget_data.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)
    datafile.write(output)
