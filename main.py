import os
import csv
main_csv = os.path.join ("..", "C:/Users/ashyg/Documents/GitHub/Python-Challenge/PyBank", "budget_data.csv")

with open(main_csv) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader)
    ### containers
    dates= []
    profit_losses= []
    average_dif = []

    for row in reader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))
### len function to count
total_months = len(dates)
## change into full messaging 
print(total_months)

## profit_losssum
total_profit_loss = sum(profit_losses)
print(total_profit_loss)

#change
for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    average_dif.append(change)

average_change = sum(average_dif)/ len(average_dif)
print(average_change)

greatest_increase = max(average_dif)
greatest_date = dates[average_dif.index(greatest_increase)+1]

print (greatest_increase)
print (greatest_date)

greatest_decrease = min(average_dif)
decrease_date = dates [average_dif.index(greatest_decrease) + 1]

print(greatest_decrease)
print(decrease_date)


###convert into financial analysis 
#with open(main_csv) as csv_file:
 #   csv_reader = csv.reader(csv_file, delimiter= ",")
  #  csv_header = next(csv_file)
   # print(f"Header: {csv_header}")
    ###simply need to count the number of rows under date 
##total_months= this is wrong 
