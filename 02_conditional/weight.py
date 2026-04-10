weight = float(input("Enter your weight"))
unit = input(" Kilogram or Pound? (K,L)")

if unit == "K":
    weight = weight *2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} is not valid")

print(f"your weight is: {weight}  {unit} ")  