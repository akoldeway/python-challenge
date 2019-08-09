import os
import csv



def main():
    # assumes csv is in PyBank folder
    budget_csv = os.path.join("PyBank","Resources", "budget_data.csv")

    with open(budget_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        next(csv_reader)
        
        number_of_months = 0
        total_amount = 0.00
        monthly_pl_changes ={} 
        previous_month_value = 0.0
        
        #loop through each row to calc summary info (# of months, total amount, monthly changes)
        for row in csv_reader:
            number_of_months +=1
            total_amount += float(row[1])
            
            #calculate the change in value from prevous month and store in dictionary
            if number_of_months > 1:

                #add month and change in profit/loss from previous month to dictionary
                monthly_pl_changes[row[0]]= float(row[1]) - previous_month_value
    
            #done with calcs, set prevous month value for next iteration
            previous_month_value = float(row[1])
            

    #find max and min values from the dictionary, and sum totals
    max_increase = max(value for value in monthly_pl_changes.values())
    max_decrease = min(value for value in monthly_pl_changes.values())
    sum_value = sum(value for value in monthly_pl_changes.values())

    #loop through profit/loss change dictory to find the months with the min and max
    for month, value in monthly_pl_changes.items():
        if value == max_increase:
            max_increase_month = month
        elif value == max_decrease:
            max_decrease_month = month

    # format final output
    final_output = []
    final_output.append("Financial Analysis")
    final_output.append("----------------------------")
    final_output.append(f"Total Months: {number_of_months}")
    final_output.append(f"Net Profit/Loss: ${total_amount:,.2f}")
    final_output.append(f"Average Monthly Profit/Loss Change: ${sum_value / len(monthly_pl_changes):,.2f}")
    final_output.append(f"Greatest Increase in Profits: {max_increase_month} (${max_increase:,.2f})")
    final_output.append(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,.2f})")

    #write results to a file
    with open("pyBank_Results.txt","w") as results_file:
        for row in final_output:
            results_file.write(row + "\n")

    #this sweet little statement will print each item in my "final output" list on a new line
    print("""{}""".format("\n".join(final_output[0:])))

    
if __name__ == "__main__":
    main()

