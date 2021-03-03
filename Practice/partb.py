employ_data = {}
employ1 = {"Employ_ID": "001", "Name": "Kashif", "Salary": 30000, "Age": 29}
employ2 = {"Employ_ID": "002", "Name": "Rashid", "Salary": 45000, "Age": 31}
employ3 = {"Employ_ID": "003", "Name": "Noman", "Salary": 50000, "Age": 35}
employ4 = {"Employ_ID": "004", "Name": "Ali", "Salary": 25000, "Age": 23}
employ5 = {"Employ_ID": "005", "Name": "Aftab", "Salary": 35000, "Age": 21}
employ6 = {"Employ_ID": "006", "Name": "Fahad", "Salary": 65000, "Age": 30}
employ7 = {"Employ_ID": "007", "Name": "Nafees", "Salary": 50000, "Age": 27}
employ_data = {"Employ_1":employ1,"Employ_2":employ2,"Employ_3":employ3,"Employ_4":employ4,"Employ_5":employ5,"Employ_6":employ6,"Employ_7":employ7}
print(employ_data)

for i in employ_data:
    e = employ_data[i]
    name = e['Name']
    salary = e['Salary']
    if int(salary) > 30000:
        print(i,") ",name," , ",salary)
