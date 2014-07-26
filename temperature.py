def convertFahrenheitToCelsius(n1):
    """Converts a temperature from Fahrenheit to Celsius."""
    return (n1 - 32.0) * 5.0 / 9.0

def convertCelsiusToFahrenheit(n1):
    """Converts a temperature from Celsius to Fahrenheit."""
    return ((n1 * 9.0 / 5.0) + 32.0)

def returnFahrenheitToCelsius(n1):
    """Returns a formatted output after performing a Fahrenheit to Celsius temperature conversion."""
    return ("{0} degrees F = {1} degrees C".format(n1, convertFahrenheitToCelsius(n1)))

def returnCelsiusToFahrenheit(n1):
    """Returns a formatted output after performing a Celsius to Fahrenheit temperature conversion."""
    return ("{0} degrees C = {1} degrees F".format(n1, convertCelsiusToFahrenheit(n1)))

inputFahrenheit = raw_input("Enter a Fahrenheit temperature:")
inputCelsius = raw_input("Enter a Celsius temperature:")
outputCelsius = returnFahrenheitToCelsius(int(inputFahrenheit))
print outputCelsius
outputFahrenheit = returnCelsiusToFahrenheit(int(inputCelsius))
print outputFahrenheit


            
            
