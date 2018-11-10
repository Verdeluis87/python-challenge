#PyBank
# Import CSV
import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    # Set the Variables
    total_net_amount=0
    total_of_months=0
    previous_value=0
    change=0
    total_change=0
    greatest_decrease=0
    greatest_increase=0

    # Iterate over the rows to find the total amount, and total of months
    for row in csvreader:
        total_of_months=total_of_months+1
        value = (int(row[1]))
        total_net_amount = total_net_amount + value
    # Calculate the change between the values for each month.
        if total_of_months >1:
            change= value-previous_value
        total_change= total_change+change
    # Find the months with both the Greatest Increase value and Greatest Decrease Value
        if greatest_decrease > change:
            greatest_decrease=change
            greatest_decrease_date=row[0]
            
        elif greatest_increase < change:
            greatest_increase=change
            greatest_increase_date=row[0]
        previous_value=value
    # Find the Avegare change for the whole period of time in the data.
    average=total_change/(total_of_months-1)
    
    def print_line(file_obj, line):
        file_obj.write(line + "\n")
        print(line)
    
    with open("results.txt","w") as f: #create add file in write mode
        print_line(f, 'Financial Analysis')
        print_line(f, '-----------------------------')
        print_line(f, f'Total of months:{total_of_months}')
        print_line(f, f'Total:${total_net_amount}')
        print_line(f, f'Average  Change: ${(average):.2f}')
        print_line(f, f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
        print_line(f, f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')  
        #writes o/p to add.txt file
    