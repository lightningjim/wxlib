# Define Units
# Temperature
s_fahrenheit = 0
s_celsius = 1
s_kelvin = 2

# Wind speed
s_mph = 0
s_knots = 1
s_kph = 2
s_ms = 3

# Pressure
s_mb = 0
s_hpa = 0
s_inmg = 2
s_mmmg = 2

def temp_conv(temp, from_unit, to_unit):
	if from_unit == s_fahrenheit:
		temp_conv = {
			s_fahrenheit : temp,
			s_celsius : 5 / 9 * (temp - 32),
			s_kelvin : 5 / 9 * (temp + 459.67)
		}
	if from_unit == s_celsius:
		temp_conv = {
			s_fahrenheit : 9 / 5 * temp + 32,
			s_celsius : temp,
			s_kelvin : temp + 273.15
		}
	if from_unit == s_kelvin:
		temp_conv = {
			s_fahrenheit : temp * 9 / 5 - 459.67,
			s_celsius : temp + 273.15,
			s_kelvin : temp
		}
	return temp_conv(to_unit, None)
