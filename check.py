meal_charge = float(input("Enter the charge for your meal: "))
tip = lambda x: x * 0.18
tax = lambda x: x * 0.07
total = lambda x: x + tip(x) + tax(x)

print(f"Meal Charge: ${meal_charge:.2f}")
print(f"Tip (18%): ${tip(meal_charge):.2f}")
print(f"Tax (7%): ${tax(meal_charge):.2f}")
print(f"Total Price: ${total(meal_charge):.2f}")
