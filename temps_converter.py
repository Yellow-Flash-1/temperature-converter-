from sys import argv

def fahrenheit_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
	return (celsius * 9 / 5) + 32

def _output(scale, temperature):
	match scale.upper():
		case 'C':
			return f"{temperature} degrees Celsius is {celsius_to_fahrenheit(temperature)} degrees Fahrenheit"
		case 'F':
			return f"{temperature} degrees Fahrenheit is {fahrenheit_to_celsius(temperature)} degrees Celsius"

		case _:
			raise ValueError

def _output_number(scale, temperature):
	match scale.upper():
		case 'C':
			return celsius_to_fahrenheit(temperature)
		case 'F':
			return fahrenheit_to_celsius(temperature)

		case _:
			raise ValueError


if __name__=="__main__":
	if len(argv) != 3:
		print("Usage: python temps_converter.py (F|C) temperature")
		exit(1)

	scale = argv[1]
	temperature = float(argv[2])

	try:
		print(_output(scale, temperature))
	except ValueError:
		print("Usage: python program.py [F|C] temperature")
