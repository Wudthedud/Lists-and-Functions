# Function to calculate average days of absence
def calculate_average(days_absent):
    total_days = sum(days_absent)
    return total_days / len(days_absent)

# Function to find the person with the most days of absence
def find_most_absent(names, days_absent):
    max_index = days_absent.index(max(days_absent))
    return names[max_index]

# Function to find names of people with zero absence
def find_zero_absence(names, days_absent):
    zero_absence_names = [names[i] for i in range(len(names)) if days_absent[i] == 0]
    return sorted(zero_absence_names)

# Function to find names with absence above average
def above_average_names(names, days_absent, average):
    above_average = [names[i] for i in range(len(names)) if days_absent[i] > average]
    return sorted(above_average)

# Main program
if __name__ == "__main__":
    names = []
    days_absent = []

    # Input loop
    while True:
        employee_name = input("Enter employee name (or $ to terminate): ")
        days = int(input("Enter the amount of days they were absent: "))
        if employee_name == "$":
            break

        # Splitting input into name and days absent
        names.append(employee_name)
        days_absent.append(days)
        print("-" * 30)

    # Calculating results
    average = calculate_average(days_absent)
    most_absent = find_most_absent(names, days_absent)
    zero_absence = find_zero_absence(names, days_absent)
    above_average = above_average_names(names, days_absent, average)

    # Printing results
    print("\nResults:")
    print(f"1. Average days of absence per year: {average:.2f} days")
    print(f"2. Person with the most days of absence: {most_absent}")
    print(f"3. People with zero absence: {', '.join(zero_absence)}")
    print(f"4. People with absence above average: {', '.join(above_average)}")
