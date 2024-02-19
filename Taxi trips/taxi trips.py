def taxi_tracking_system():
    # Get driver's name
    driver_name = input("Enter the driver's name: ")

    # Variables to keep track of daily details
    total_time = 0
    total_income = 0
    trip_count = 0

    while True:
        start_new_trip = input("Do you want to start a new trip? (yes/no): ").lower()

        if start_new_trip == "no":
            # End of the day, print summary
            print("\nSummary for", driver_name)
            print("Total time of all trips: {} minutes".format(total_time))
            print("Average time of all trips: {} minutes".format(total_time / trip_count) if trip_count > 0 else "No trips taken")
            print("Total income for the day: ${}".format(total_income))
            print("Average cost of all trips: ${}".format(total_income / trip_count) if trip_count > 0 else "No trips taken")
            break

        elif start_new_trip == "yes":
            try:
                # Get the time the trip took in minutes
                trip_time = int(input("Enter the time the trip took in minutes: "))

                if trip_time < 0:
                    print("Error: Trip time cannot be negative. Please enter a valid value.")
                    continue

                # Calculate cost for the trip
                trip_cost = 10 + 2 * trip_time

                # Update daily details
                total_time += trip_time
                total_income += trip_cost
                trip_count += 1

                # Print cost for the current trip
                print("Cost for the trip: ${}".format(trip_cost))

            except ValueError:
                print("Error: Invalid input. Please enter a valid integer for trip time.")

        else:
            print("Error: Invalid input. Please enter 'yes' or 'no'.")

taxi_tracking_system()
