#Display available vehicles with their details.
def display_vehicles(vehicles, seats_needed):
    print("\nVEHICLE NUMBER - TYPE - NO. SEATS")
    for i, vehicle in enumerate(vehicles, start=1):
        if vehicle[1] < seats_needed:
            print(f"No. {i} - {vehicle[0]} - {vehicle[1]} seats - NOTE: Not enough seats")
        else:
            print(f"No. {i} - {vehicle[0]} - {vehicle[1]} seats")

# Main function to run the vehicle booking system.
def main():
    vehicles = [
        ("Suzuki Van", 2),
        ("Toyota Corolla", 4),
        ("Honda CRV", 4),
        ("Suzuki Swift", 4),
        ("Mitsubishi Airtrek", 4),
        ("Nissan DC Ute", 4),
        ("Toyota Previa", 7),
        ("Toyota Hi Ace", 12),
        ("Toyota Hi Ace", 12),
    ]

    booked_vehicles = []

    while True:
        seats_needed = int(input("Please enter the number of seats required (Type -1 to quit): "))
        if seats_needed == -1:
            break
        display_vehicles(vehicles, seats_needed)
        vehicle_number = int(input("Enter a number to book: "))
        if 1 <= vehicle_number <= len(vehicles):
            selected_vehicle = vehicles[vehicle_number - 1]

            if selected_vehicle[1] >= seats_needed:
                name = input("Enter your name: ")
                print(f"{selected_vehicle[0]} booked by {name}\n")
                booked_vehicles.append((selected_vehicle[0], name))
                vehicles.pop(vehicle_number - 1)
            else:
                print(f"{selected_vehicle[0]} is not available\n")
        else:
            print("Invalid vehicle number. Please try again.\n")

    print("\nVEHICLES BOOKED TODAY")
    for i, booked_vehicle in enumerate(booked_vehicles, start=1):
        print(f"No. {i} - {booked_vehicle[0]} - Booked by: {booked_vehicle[1]}")

main()
