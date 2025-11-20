# Shopping cart using dictionary

cart = {
    "apple": 3,
    "banana": 5,
    "orange": 2
}

# Access values
print("Apples in cart:", cart["apple"])
print("Bananas in cart:", cart.get("banana"))

# Add and update
cart["grape"] = 4          # add new item
cart["apple"] = 6          # update existing item

# Loop through items
print("\nCart contents:")
for item, qty in cart.items():
    print(item, ":", qty)

# Remove an item
cart.pop("orange")
print("\nAfter removing orange:", cart)

# Nested dictionary for multiple users
users_cart = {
    "user1": {"apple": 2, "banana": 1},
    "user2": {"grape": 3, "apple": 1}
}

print("\nUser2's grapes:", users_cart["user2"]["grape"])
