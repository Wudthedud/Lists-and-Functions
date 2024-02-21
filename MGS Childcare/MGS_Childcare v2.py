namesList = []
hourlyCost = 12
repeat = True

# Checks in child, adds name to roll
def checkin():
    name = input("Enter your child's name: ").title().strip()
    namesList.append(name)
    print(f"{name} has been added to the roll\n")
    print("-" * 30)

# Removes names from roll
def checkout():
    name = input("Enter your child's name: ").title().strip()
    try:
        namesList.remove(name)
        print(f"{name} has been removed from the roll\n")
    except:
        print(f"{name} is not in the roll")
        print("-" * 30)

# Calculates cost for amount of hours
def cost():
    try:
        hours = int(input("Enter amount of hours: "))
        print(f"Your child was here for {hours} hours, at ${hourlyCost} an hour, the charge is ${int(hours)*hourlyCost}\n")
        print("-" * 30)
    except:
        print("Please enter the number of hours as an integer! ")
        print("-" * 30)

def roll():
    if len(namesList) > 0:
        print(namesList)
    else:
        print("There is no one in the roll")

def main():
    print("Welcome to MGS childcare, please select and option to continue: ")
    while repeat == True:
        mode = input("[1] Drop off a child\n[2] Pick up a child\n[3] Calculate cost\n[4] Print roll\n[5] Exit the syetem\n")
        print("-" * 30)
        if mode == "1": 
            checkin()
        elif mode == "2":
            checkout()
        elif mode == "3":
            cost()
        elif mode == "4":
            roll()
        elif mode == "5":
            print("Thank you for visiting MGS Childcare")
            break
        else:
            print("Please enter a number between 1-5")
main()