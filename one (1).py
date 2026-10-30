
# ============================================================
# Unit Conversion System (Short Version) - PS 16
# ============================================================

# Function to convert length units (Kilometers and Miles)
def convert_length(v, o):
    if o == 1:
        return f"{v:g} km = {v * 0.621371:.2f} miles"
    elif o == 2:
        return f"{v:g} miles = {v / 0.621371:.2f} km"
    else:
        return "Invalid option. Select 1 or 2."


# Function to convert weight units (Kilograms and Grams)
def convert_weight(v, o):
    if o == 1:
        return f"{v:g} kg = {v * 1000:.2f} g"
    elif o == 2:
        return f"{v:g} g = {v / 1000:.2f} kg"
    else:
        return "Invalid option. Select 1 or 2."


# Function to convert temperature units (Celsius and Fahrenheit)
def convert_temperature(v, o):
    if o == 1:
        return f"{v:g} C = {v * 9 / 5 + 32:.2f} F"
    elif o == 2:
        return f"{v:g} F = {(v - 32) * 5 / 9:.2f} C"
    else:
        return "Invalid option. Select 1 or 2."


# Function to convert time units (Hours and Minutes)
def convert_time(v, o):
    if o == 1:
        return f"{v:g} hours = {v * 60:.2f} minutes"
    elif o == 2:
        return f"{v:g} minutes = {v / 60:.2f} hours"
    else:
        return "Invalid option. Select 1 or 2."


# ============================================================
# Main Program
# ============================================================

# Display the unit conversion menu
print("===== UNIT CONVERSION SYSTEM =====")
print("1. Length      (1: km to miles, 2: miles to km)")
print("2. Weight      (1: kg to g, 2: g to kg)")
print("3. Temperature (1: C to F, 2: F to C)")
print("4. Time        (1: hours to minutes, 2: minutes to hours)")

# Accept and validate the user's category choice
choice = input("Enter your choice (1-4): ")

if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Select 1 to 4.")
    exit()

# Accept the conversion direction
option = int(input("Select conversion (1 or 2): "))

# Accept the input value and handle invalid numeric input
try:
    value = float(input("Enter value: "))
except ValueError:
    print("Invalid value. Enter a number.")
    exit()

# Perform the selected unit conversion and display the result
if choice == "1":
    print(convert_length(value, option))
elif choice == "2":
    print(convert_weight(value, option))
elif choice == "3":
    print(convert_temperature(value, option))
else:
    print(convert_time(value, option))
