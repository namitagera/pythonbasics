temperature = 75
forecast = "rainy"

if temperature < 80 or temperature > 60:
    print("It's too hot.")
elif temperature < 60:
    print("It's too cold")
else:
    print("Have a good day")

if temperature < 80 and forecast != "rainy":
    print("Go outside")
else:
    print("Stay in")

if not forecast == "rainy":
    print("Go outside")
else: 
    print("Stay in")

raining = True

if raining:
    print("Stay in")

if not raining:
    print("Go out")
else:
    print("Stay in")