while True:
    try:
        kilometers = float(input("kilometers = "))
        break

    except ValueError:
        print ("Invalid input, please repeat.")

print(f"\nkilometers = {kilometers}")
miles = kilometers / 0.621371
miles_2 = format (miles, ".2f")
print (f"miles = {miles_2}")