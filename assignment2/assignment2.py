import csv
import os
import custom_module
from datetime import datetime

# Task 2

def read_employees():
    dict = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            first_row = True

            for row in reader:
                if first_row:
                    dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")

    dict["rows"] = rows
    return dict

employees = read_employees()
print(employees)

# Task 3

def column_index(column_name):
    index = employees["fields"].index(column_name)
    return index

employee_id_column = column_index("employee_id")

# Task 4

def first_name(row_number):
    index = column_index("first_name")
    name = employees["rows"][row_number][index]
    return name

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

# Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]
print(sort_by_last_name())

# Task 8

def employee_dict(row):
    dict_result = {}

    for field in employees["fields"]:
        if field != "employee_id":
            index = column_index(field)
            dict_result[field] = row[index]

    return dict_result

# Task 9

def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)

    return result

# Task 10

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Task 12 
def read_minutes():
    def read_file(filename):
        result = {}
        rows = []

        with open(filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if "fields" not in result:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))
        result["rows"] = rows
        return result

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)

# Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1.union(set2)

    return combined_set


minutes_set = create_minutes_set()

# Task 14
def create_minutes_list():
    minutes = list(minutes_set)

    converted = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes
    ))

    return converted


minutes_list = create_minutes_list()

print(minutes_list)

# Task 15

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    sorted_list = list(map(
        lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")),
        minutes_list
    ))

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(sorted_list)

    return sorted_list


print(write_sorted_list())