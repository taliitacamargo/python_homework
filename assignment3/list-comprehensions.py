#Task 3
import csv


def read_employees():
    try: 
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            read_rows = list(reader)
            return read_rows
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")

rows = read_employees()


names = [row[1] + " " + row[2] for row in rows[1:]]
print(names)

e_names = [name for name in names if "e" in name.lower()]
print(e_names)
