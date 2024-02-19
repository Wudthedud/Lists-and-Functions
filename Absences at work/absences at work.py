def input_data():
    employees = []
    while True:
        input_str = input("Enter employee data (name days_absent) or $ to finish: ")
        if input_str == "$":
            break
        else:
            employee_data = input_str.split()
            name = " ".join(employee_data[:-1])
            days_absent = int(employee_data[-1])
            employees.append((name, days_absent))
    return employees


def calculate_average(employees):
    total_days = sum(days for _, days in employees)
    average = total_days / len(employees)
    return average


def find_most_absent(employees):
    max_absent = max(employees, key=lambda x: x[1])
    return max_absent[0]


def find_not_absent(employees):
    not_absent = [name for name, days in employees if days == 0]
    return not_absent


def find_above_average(employees, average):
    above_average = [f"{name} {days}" for name, days in employees if days > average]
    return above_average


def print_results(average, most_absent, not_absent, above_average):
    print("\nAverage number of days staff were absent:", f"{average:.2f}")
    print("Person with most days absent:", f"{most_absent} with {employees_dict[most_absent]} days")
    
    print("\nList of people not absent at all:")
    for name in not_absent:
        print(name)
    
    print("\nList of people absent above average:")
    for entry in above_average:
        print(entry)


# Main program
employees = input_data()
average_days_absent = calculate_average(employees)
most_absent_person = find_most_absent(employees)
not_absent_people = find_not_absent(employees)
above_average_list = find_above_average(employees, average_days_absent)

print_results(average_days_absent, most_absent_person, not_absent_people, above_average_list)
