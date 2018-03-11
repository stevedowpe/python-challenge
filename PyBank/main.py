# Dow-PyBank

# Initial imports, empty lists, and setting of initial variables ---------------------------------
import os
import csv
revenue = []
change_revenue = []
previous_revenue = 0
total_revenue = 0

# Define path to csv, read the csv path, save values of csv to variable ----------------------------------
csvpath = os.path.join('raw_data', 'budget_data_1.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

# Start the Loop -------------------------------------------------------------------------------------  
    for row in csvreader:
        #print(row)
        
# STEP 1 - DETERMINE TOTAL NUMBER OF MONTHS ----after several attempt, found this on stackoverflow---------------
        #row_count = sum(1 for row in csvfile)
        #print("Total Months: " + str(row_count))

# STEP 2 - DETERMINE TOTAL REVENUE FOR THE ENTIRE PERIOD --------------------------------------------------------
        #print(row[1])
        total_revenue = total_revenue + int(row[1])
        revenue.append(int(row[1]))

# STEP 3 -- DETERMINE AVERAGE CHANGE IN REVENUE BETWEEN MONTHS OVER THE ENTIRE PERIOD ------(Luis helped with this part via Google Hangout)-----
        change_revenue_variable = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
   
        change_revenue.append(change_revenue_variable)
        
        #change_revenue_row = (row[0])
        #change_revenue.append(change_revenue_row)



# Final Printout of Info ----------------------------------------
    #print(total_revenue)
    #print(previous_revenue)
    #print(len(revenue))
    #print(revenue)
    
    #print(sum(revenue))
    average_revenue = float(sum(revenue))/(len(revenue))
    #print(average_revenue)

    average_revenue_change = float(sum(change_revenue))/(len(change_revenue))
    #print(average_revenue_change)
    
    #print(max(change_revenue))
    #print(min(change_revenue))

    print("Financial Analysis")
    print("_______________________________")
    print("Total Months: " + str(len(revenue)))
    print("Total Revenue: $" + str(total_revenue))
    print(("Average Revenue Change: $" + str(average_revenue_change)))
    print("Greatest Increase in Revenue: ____" + "($"+ str(max(change_revenue))+")")
    print("Greatest Decrease in Revenue: ____" + "($"+ str(min(change_revenue))+")")
