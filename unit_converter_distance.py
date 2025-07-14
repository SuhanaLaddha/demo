print("1. Km to Miles\n2. Miles to Km\n3. Celsius to Fahrenheit\n4. Fahrenheit to Celsius")
choice = int(input("Choose conversion type (1–4): "))

if choice == 1:
    km = float(input("Enter distance in km: "))
    print(f"{km} km = {km * 0.621371:.2f} miles")
elif choice == 2:
    miles = float(input("Enter distance in miles: "))
    print(f"{miles} miles = {miles / 0.621371:.2f} km")
elif choice == 3:
    c = float(input("Enter temperature in °C: "))
    print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")
elif choice == 4:
    f = float(input("Enter temperature in °F: "))
    print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")
else:
    print("❌ Invalid choice")
