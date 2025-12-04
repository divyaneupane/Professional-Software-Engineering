def temperature_convertor():
    temp=input("Enter the temperature: ")
    
    #validation: must start with 'F' OR 'C' followed by digits
    
    if len(temp) < 2 or temp[0] not in ['F', 'C']:
        print("Invalid input. Must start with C or F.")
        
    prefix=temp[0].upper()        
        

    try:
        value = float(temp[1:])  # allows decimal numbers
        print(f"Valid input: {temp[0]}{value}")
    except ValueError:
        print("Invalid number after prefix. Please enter a valid number.")
            
    #Conversion Fahrenheit → Celsius
    if prefix == 'F':
        celsius = (value - 32) * 5 / 9
        print(f"F{value:.0f} degrees Fahrenheit is converted to {celsius:.2f} degrees Celsius")

    #  Celsius → Fahrenheit
    elif prefix == 'C':
        
        fahrenheit = (value * 9 / 5) + 32
        print(f"C{value:.0f} degrees Celsius is converted to {fahrenheit:.2f} degrees Fahrenheit")

# Run the converter
temperature_convertor()