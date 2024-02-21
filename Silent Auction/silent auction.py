def silent_auction():
    # Get auction details from the auction manager
    item = input("What is the auction for? ")
    try: 
        reserve_price = float(input("What is the reserve price? "))
    except:
        print("You have not entered a number, the bidding will start at $0")
        reserve_price = 0

    print("-" * 30)
    print(f"The auction for the {item} has started! Type '-1' to end auction.")

    highest_bid = 0

    while True:
        print("-" * 30)
        print(f"\nHighest bid so far is ${highest_bid}")

        bid_input = input("What is your bid? ")

        # Check for termination signal
        if bid_input == '-1':
            break

        try:
            bid = float(bid_input)
        except ValueError:
            print("Invalid input. Please enter a valid bid or 'end' to end the auction.")
            continue

        # Check if bid is higher than the highest bid
        if bid > highest_bid:
            highest_bid = bid
            print(f"Highest bid so far is ${highest_bid}")
            
        else:
            print(f"Please enter a higher bid than ${highest_bid}")

    # Check if the highest bid meets the reserve price
    if highest_bid >= reserve_price:
        print(f"\nThe auction for the {item} finished with a bid of ${highest_bid}")
    else:
        print(f"\nThe auction for the {item} didn't sell. The highest bid was ${highest_bid}, which did not meet the reserve price of ${reserve_price}")

# Run the silent auction program
silent_auction()
