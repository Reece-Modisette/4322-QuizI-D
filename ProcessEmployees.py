'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file
infile = open("employee_data.csv", "r")

csr = csv.reader(infile)

next(csr)

# create an empty dictionary
csr_dict = {}

# use a loop to iterate through the csv file
for row in csr:
    # assign variable names
    emp_id = row[0]
    fname = row[1]
    lname = row[2]
    dept = row[3]
    title = row[4]
    salary = float(row[5])

# check if the employee fits the search criteria

    if title == 'CSR':
        name = fname+" "+lname
        cur_sal = salary,
        new_sal = int(salary * 1.10)
        print(new_sal)
        csr_dict[name] = {
            "Salary": new_sal, }

        print("\n\n")
        print("Manager Name:", name)
        for i, j in csr_dict[name].items():
            print(i + ":", j)
print()
print('=========================================')
print()

print(csr_dict)

# iternate through the dictionary and print out the key and value as per printout
