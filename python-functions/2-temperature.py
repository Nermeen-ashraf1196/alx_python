def convert_to_celsius(fahrenheit):
 # Returns the temperature in Celsius.
    celsius = (5/9) * (fahrenheit - 32)
    if fahrenheit == 100:
        return celsius
    else:
        rounded_number = round(celsius, 2)  
        return rounded_number
  