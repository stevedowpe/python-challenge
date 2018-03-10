# Dow-PyBank

# STEP 0 - READ IN THE LIST ----------------------------------------------------------------------
# A1 - Import operating systems and csv capability
import os
import csv

# A2 - Define empty lists for future
revenue = []

# B - Create path to the csv file ---------- 
csvpath = os.path.join('raw_data', 'budget_data_1.csv')

# C - Read the CSV file via the CSV module -------------
with open(csvpath, newline='') as csvfile:

# D - Store the CSV file as a variable ----------------
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Each row is read as a row
    # Dow - note to self <<Don't understand  this part>>
    for row in csvreader:
        #print(row)
        #print(len(row))
    #print("The above is the data... now on to Step 1:")
    #print("______________________________")

# STEP 1 - DETERMINE TOTAL NUMBER OF MONTHS --------------------------------------------------------
        # DOW - THESE BELOW ARE ALL ATTEMPTS THAT DID NOT WORK:
                    #csvreader.sum = sum -->
                    #print(sum)

                    #for x in range(csvreader)
                    #print (x)

                    #rows = len (cvsreader)
                    #print(rows)

                    #csvlength = [csvreader]
                    #print len(csvlength)
                    #len(csvreader)
                    #count_rows = count(rows)
                    #print(count_rows)

                    #month_number = len(csvreader)
                    #print(month_number)

                    #row_count = sum(row)
                    #print(row_count)

                    #totalmonth = 0
                    #for row in csvreader:
                    #totalmonth = totalmonth + 1
                    #print(totalmonth)

        # THIS ONE BELOW - FROM STACKOVERFLOW - DID WORK:
    
    #csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader) 
    
    #for row in csvreader:
        row_count = sum(1 for row in csvfile)
        #print(row_count)

        print("Total Months: " + str(row_count))

# STEP 2 - DETERMINE TOTAL REVENUE FOR THE ENTIRE PERIOD --------------------------------------------------------
        # DOW - THESE BELOW ARE ALL ATTEMPTS THAT DID NOT WORK:
                    # with open("file.csv") as fin:
                    # fin.next()
                    # total = sum(int(r[1]) for r in csv.reader(fin))

                    #csvfile.next()
                    #total = sum(int(r[1]) for r in csv.reader(csvfile))

                    # import csv
                    # with open('infant_mortality.csv', 'r') as f:
                    # next(csvfile) #skips the first row
                    # total = 0
                    # for row in csv.reader:
                    #    total = float(row[1])
                    # print('The total is {}'.format(total))
        
        revenue.append(row[1])
        for row in revenue:
            print(revenue)

        #total_revenue = sum(revenue)
        #print(total_revenue)
        #total_revenue = total_revenue + revenue(row)
        #print(total_revenue)

        #skip headers
        #next(csvreader, None)
        #total_revenue = total_revenue + csvfile((int(row[1]))
        #print(total_revenue)