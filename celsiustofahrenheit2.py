def celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

celsius = float(input("Enter the temperture in celsius: "))
if(celsius < -273.15):
    print("Not possible to get a temperture lower than -273.15C")
else:
    print(celsius_to_fahrenheit(celsius))
