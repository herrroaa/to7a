import csv
import os

csv_path = os.path.join("Resources", "employees.csv")
output_path = os.path.join("output", "new_employee_data.csv")

with open(csv_path, newline="") as csvfile:

    reader = csv.DictReader(csvfile)
    new_employee_list = []
    
    for row in reader:
        
        email_address = row["First Name"] + "." + row["Last Name"] + "@example.com"
        new_employee_info = {
                                "First Name": row["First Name"],
                                "Last Name": row["Last Name"],
                                "SSN": row["SSN"],
                                "Email": email_address
                            }
        new_employee_list.append(new_employee_info)

with open(output_path, "w", newline="") as outputfile:

    fieldnames = ["First Name", "Last Name", "SSN", "Email"]
    writer = csv.DictWriter(outputfile, fieldnames)

    writer.writeheader()
    writer.writerows(new_employee_list)