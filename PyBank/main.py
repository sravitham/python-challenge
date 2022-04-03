# Import the necessary dependencies for os.path.join()
import os
import csv


# Read in a .csv file
csv_path = "PyBank/Resources/budget_data.csv"

with open(csv_path) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    
    #To keep an index of all the months
    months_index = []
    #To track of all the changes in profit and losses between each month
    All_changes_in_pl = []


    total_months = 0
    total_profitloss = 0
    total_change_in_pl = 0
    current_pl = 0

    for row in csv_reader:
        total_months += 1

        months_index.append(row[0])

        total_profitloss = total_profitloss + int(row[1])

        final_pl = int(row[1])
        monthly_change_pl = final_pl - current_pl
        if total_months == 1:
            first_pl= int(row[1])
        else:
            first_pl == first_pl
        All_changes_in_pl.append(monthly_change_pl)

        sum_pl = (sum(All_changes_in_pl) - first_pl)
        current_pl = final_pl

        average_change = (sum_pl/total_months)

        greatest_increase_profits = max(All_changes_in_pl)
        greatest_decrease_profits = min(All_changes_in_pl)

        greatest_increase_date = months_index[All_changes_in_pl.index(greatest_increase_profits)]
        greatest_decrease_date = months_index[All_changes_in_pl.index(greatest_decrease_profits)]
print(All_changes_in_pl)
# print(sum_pl)
print(first_pl)
print(f"Total Months: {str(total_months)}")

print(f"Total Profits: ${total_profitloss}")

print(f"Average Change: ${average_change}")

print(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase_profits}")

print(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease_profits}")

