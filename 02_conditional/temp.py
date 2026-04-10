unit = input("Is the temp is in °C or °F ? (C/F)")
temp = float(input("Enter the Temp you want to change"))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"The temp in fahrenhit is {temp}°F")
    
elif unit == "F": 
    temp = round((temp - 32) * 5 / 2 )
    print(f"The temp in Celsius is {temp}°C")

else :
    print(f"{unit} is not valid")