# PyBoss
import os
import csv

employee_id = []
first = []
last = []
year = []
month = []
day = []
SSN1 = []
SSN2 = []
SSN3 = []

states_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

# Define the csv path for imported data
csvpath_in = os.path.join('raw_data','employee_data1.csv')

# Read the data from the csv path
with open(csvpath_in, 'r', encoding="utf-8") as csvfile_in:

    # Create a variable for the data in our program
    csvreader_in = csv.reader(csvfile_in, delimiter=',')
    next(csvreader_in, None)

    for row in csvreader_in:
        #print(row)
        employee_id.append(int(row[0]))

        name = row[1].split(" ")
        first.append(name[0])
        last.append(name[1])

        date = row[2].split("-")
        year.append(date[0])
        month.append(date[1])
        day.append(date[2])

        SSN = row[3].split("-")
        SSN1.append(SSN[0])
        SSN2.append(SSN[1])
        SSN3.append(SSN[2])

        # <<Steve Dow Note - Tried to get to print as indicated here, instead sent to output file>>: print(str(employee_id[row], first[row], last[row], month[row],"/", day[row], "/", year[row], "***-**-", SSN3[row])) 
    

# Zip lists together
cleaned_csv = zip(employee_id, first, last, month, day, year, SSN3)
print(cleaned_csv)

#<<Steve Dow Note: - Tried to build in the ***-**>>: cleaned_csv_2 = zip(employee_id, first, last, month, day, year, "***-**-" + str(SSN3))
#print(cleaned_csv_2)

#Set variable for output file
output_file = os.path.join("Dow_PyBoss_output.csv")

# Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Employee ID", "First Name", "Last Name", "Month", "Day", "Year", "Last 4 of SSN"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)

    




