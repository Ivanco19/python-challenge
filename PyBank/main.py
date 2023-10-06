# Import libraries
import csv, os

# Filepath of our database
file_path = os.path.join('.','PyBank\Resources', 'budget_data.csv')

with open(file_path) as budget:
    csv_iterable = csv.reader(budget)

    #We skip the header and store values in a variable
    header = next(csv_iterable)
    
    #We skip the next line of code and will store as our first month
    first_month = previous_month = next(csv_iterable)
    total = 0

    # We create two list to store the difference between previous month and current month (diferences)
    diferences = []
    month = []
    
    for current_month in csv_iterable:
        # We acumulate the total of the profit/loss in a variable
        total = total + float(current_month[1])

        # We get the difference and add the value to 'differences' list. We store the month at the same time
        diference = float(current_month[1]) - float(previous_month[1])
        diferences.append(diference)
        month.append(current_month[0])

        # Need to set the current month to previous month variable for next iteration
        previous_month = current_month
       
    # This code gets totals (max, min and average)
    total = total + float(first_month[1])
    max_value = max(diferences)
    min_value = min(diferences)
    average = sum(diferences) / len(diferences)
    
    # We print the results in the terminal
    print('Financial Analysis')
    print('--------------------------')
    print(f'Total months: {len(month)+1}')
    print(f'Total: ${total}')
    print(f'Average change: ${round(average,2)}')
    # We get the month index using this code: diferences.index(value)
    print(f'Greatest Increase in Profits: {month[diferences.index(max_value)]} ({max_value})')
    print(f'Greatest Decrease in Profits: {month[diferences.index(min_value)]} ({min_value})')

# This code exports the results to an txt file
with open('pybank_results.txt', 'w') as my_writer:
    my_writer.write('Financial Analysis \n')
    my_writer.write('-------------------------- \n')
    my_writer.write(f'Total: ${total} \n')
    my_writer.write(f'Average change: ${round(average,2)} \n')
    my_writer.write(f'Greatest Increase in Profits: {month[diferences.index(max_value)]} ({max_value}) \n')
    my_writer.write(f'Greatest Decrease in Profits: {month[diferences.index(min_value)]} ({min_value}) \n')
