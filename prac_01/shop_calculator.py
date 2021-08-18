"""
CP1404 Practical
Program that works out the total price for a group of different items.
"""

total_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    item_price = float(input("Price of item: $"))
    total_cost += item_price
if total_cost > 100:
    total_cost *= 0.90
print(f"Total price for {number_of_items} item/s is ${total_cost:.2f}")
