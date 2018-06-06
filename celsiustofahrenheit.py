def celsius_to_fahrenheit(celsius):
    fahrenheit = int(celsius) * 9 / 5 + 32
    return fahrenheit

celsius = input("Enter the temperture in celsius: ")
print(celsius_to_fahrenheit(celsius))