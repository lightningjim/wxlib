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
s_inmg = 1
s_mmmg = 2

def temp_conv(temp, from_unit, to_unit):
	if from_unit == s_fahrenheit:
		if to_unit == s_fahrenheit:
			return temp
		elif to_unit == s_celsius:
			return 5 / 9 * (temp - 32)
		elif to_unit == s_kelvin:
			return 5 / 9 * (temp + 459.67)
		else:
			return None

	elif from_unit == s_celsius:
		if to_unit == s_celsius:
			return temp
		elif to_unit == s_kelvin:
			return temp + 273.15
		elif to_unit == s_fahrenheit:
			return 9 / 5 * temp + 32
		else:
			return None

	elif from_unit == s_kelvin:
		if to_unit == s_kelvin:
			return temp
		elif to_unit == s_fahrenheit:
			return temp * 9 / 5 - 459.67
		elif to_unit == s_celsius:
			return temp + 273.15
		else:
			return None
	else:
		return None

def wind_conv(speed, from_unit, to_unit):
	if from_unit == s_mph:
		if to_unit == s_mph:
			return speed
		elif to_unit == s_knots:
			return 1069.344 / 1852 * speed
		elif to_unit == s_kph:
			return 1.609344 * speed
		elif to_unit == s_ms:
			return 0.44704 * speed
		else:
			return None
	elif from_unit == s_knots:
		if to_unit == s_knots:
			return speed
		elif to_unit == s_kph:
			return 1.852 * speed
		elif to_unit == s_ms:
			return 1852.0 / 3600 * speed
		elif to_unit == s_mph:
			return 1.852 / 1.609344 * speed
		else:
			return None
	elif from_unit == s_kph:
		if to_unit == s_kph:
			return speed
		elif to_unit == s_ms:
			return 1 / 3.6 * speed
		elif to_unit == s_mph:
			return 1 / 1.609344 * speed
		elif to_unit == s_knots:
			return 1 / 1.852 * speed
		else:
			return None
	elif from_unit == s_ms:
		if to_unit == s_ms:
			return speed
		elif to_unit == s_mph:
			return 1 / 0.44704 * speed
		elif to_unit == s_knots:
			return 3.6 / 1.852 * speed
		elif to_unit == s_kph:
			return 3.6 * speed
		else:
			return None
	else:
		return None

def rh_from_dp(temp, dp):
	return 100 * (math.exp(17.625 * dp) / (243.04 + dp)) / math.exp((17.625 * temp) / (243.04 + temp))

def gkg_from_dp(dp, pres):
	v = 1 - ((dp.toK()) / 647.096)
	pw = 220640 * log((647.906 / dp.toK()) * -7.85951783 * v * + 1.84408259 * power(v,1.5) - 11.7866497 * power(v,3) + 22.6807411 * power(v,3.5) - 15.9618719 * power(v,4) + 1.80122502 * power(v,7.5))
	return 621.9907 * pw / (pres - pw)