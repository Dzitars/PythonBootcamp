import art
print(art.logo)

# TODO-1: Ask the user for input
print("Welcome to the secret auction program.")
bidding = True
bids = {}

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))

    # TODO-2: Save data into dictionary {name: price}
    bids[name] = bid
    # TODO-3: Whether if new bids need to be added
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ")
    print("\n" * 20)
    if more_bids == 'no':
        bidding = False

# TODO-4: Compare bids in dictionary
max(bids, key=bids.get)

max_bid_key = max(bids, key=bids.get) # This gets max value from a dictionary
max_bid_value = bids[max_bid_key]

# manual way of finding max value if not using max() function
# max_bid_key = ""
# max_bid_value = 0
#
# for key in bids:
#     if bids[key] > max_bid_value:
#         max_bid_key = key
#         max_bid_value = bids[key]

print(f"The winner is {max_bid_key} with a bid of ${max_bid_value}!")
