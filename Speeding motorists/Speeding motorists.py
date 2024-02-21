speeders = []
total_fines = 0

# 
def calculate_fine(amount_over_limit):
    if amount_over_limit < 10:
        return 30
    elif 10 <= amount_over_limit <= 14:
        return 80
    elif 15 <= amount_over_limit <= 19:
        return 120
    elif 20 <= amount_over_limit <= 24:
        return 170
    elif 25 <= amount_over_limit <= 29:
        return 230
    elif 30 <= amount_over_limit <= 34:
        return 300
    elif 35 <= amount_over_limit <= 39:
        return 400
    elif 40 <= amount_over_limit <= 44:
        return 510
    else:
        return 630

while True:
    print("-" * 30)
    name = input("Enter name of speeder (type 'stop' to end input mode): ")
    if name.lower() == 'stop':
        break
    try:
        amount_over_limit = int(input("Enter the amount over the speed limit: "))

        fine = calculate_fine(amount_over_limit)
        total_fines += fine

        if name.lower() in ['james wilson', 'helga norman', 'zachary conroy']:
            print(f"{name.upper()} - WARRANT TO ARREST")
        else:
            print(f"{name} to be fined ${fine}")

        speeders.append({'Name': name, 'Amount Over Limit': amount_over_limit})
    except: 
        print("Please enter a number")

print("\nTotal fines:", len(speeders))
for i, speeder in enumerate(speeders, 1):
    print(f"{i}) Name: {speeder['Name']} --- Amount Over Limit: {speeder['Amount Over Limit']}")
print("\nTotal amount of fines: ${}".format(total_fines))
