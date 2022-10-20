def convert_from_fahrenheit_to_celsius(x_in_fahrenheit):
    return (5/9)*(x-32)
for x in range(0, 101, 10):
    print("The conversion of {:>3} F to celcius is: {:>6.2f} C".format(x, convert_from_fahrenheit_to_celsius(x_in_fahrenheit))

