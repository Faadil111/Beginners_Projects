#Definition of the converting to Celsius function
def celsius_to_fahrenheit(celsius):
    print(celsius * 9 / 5 + 32)

#Definition of the converting to Farenheit function
def fahrenheit_to_celsius(fahrenheit):
   print((fahrenheit - 32) * 5 / 9)

# Our main Temperature converter function
def temp_conv():

# This is the while loop that helps us start our function
    while True:
        print("Enter q to Quit")
        temp = input("Enter Temperature in Celsius or Fahrenheit: ")
# These conditionals take in inputs and evaluate how the program will be executed per each input
        if temp == "q":
            print("Thanks for testing me out")
            break
# If our input is an int or a float our function will take it and evaluate
        try:
            temp = float(temp)

        # If not, it produces this error message
        except ValueError:
            print("Invalid Input")
            continue

# The program asks you whether your input was either in celcius or Farenheit, based o that it can make the following
       # calculations below
        confirm = input("What was the temperature? (C/F): ").lower()

        if confirm == "c":
            if temp < -273.15 or temp > 10000:
                print("That temperature is not possible")
            else:
                celsius_to_fahrenheit(temp)

        elif confirm == "f":
            if temp < -459.67 or temp > 10000:
                print("That temperature is not possible")
            else:
                fahrenheit_to_celsius(temp)

        else:
            print("Invalid temperature unit")

# This more of behaves sort of like our main screen when sa=tarting our temperature converter
starter = input("Press Enter to start the Temperature Converter or type 'e' to exit: ").lower()
if starter == "e":
    print("Thanks for playing :)")
else:
    temp_conv()