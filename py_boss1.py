import os
import csv
import datetime

csvpath = os.path.join("employee_data.csv")
with open(csvpath, newline='') as csvfile:
 csvreader = csv.reader(csvfile, delimiter=',')
 
 us_state_abbrev = {
         'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }    

 emp_ids = []
 emp_first_names = []
 emp_last_names = []
 emp_dobs = []
 emp_ssns = []
 emp_states = []
 
 for row in csvreader:
   emp_ids = emp_ids + [row[0]]
   split_name = row[1].split(" ")
 
 emp_first_names = emp_first_names + [split_name[0]]
 emp_last_names = emp_last_names + [split_name[1]] 
 
 reformatted_dob = datetime.datetime.strptime(row[2], "%Y-%m-%d")
 reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")
 
 emp_dobs = emp_dobs + [reformatted_dob]

 split_ssn = list(row[3])
 split_ssn[0:3] = ("*", "*", "*")
 split_ssn[4:6] = ("*", "*")
 joined_ssn = "".join(split_ssn)
 
 emp_ssns = emp_ssns + [joined_ssn]
 state_abbrev = us_state_abbrev[row[4]]
 emp_states = emp_states + [state_abbrev]
 
 empdb = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)
 
 with open("newdata.csv", "w", newline="") as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Emp ID", "First Name", "Last Name",
                      "DOB", "SSN", "State"])
     writer.writerows(empdb)