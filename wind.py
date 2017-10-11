import conversion as conv
class wind(object):

	def __init__(self, direction, dir_str, speed, units, gusts):
		self.direction = direction
		self.direction_string = dir_str
		self.speed = speed
		self.units = units
		self.gusts = gusts

		if dir_str is None:
			val=int((direction/22.5)+.5)
			arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
			self.direction_string = arr[(val % 16)]

	def toMPH(self, speed):
		return conv.wind_conv(speed,self.units,conv.s_mph)
	def toKnots(self, speed):
		return conv.wind_conv(speed,self.units,conv.s_knots)
	def toKPH(self, speed):
		return conv.wind_conv(speed,self.units,conv.s_kph)
	def toMS(self, speed):
		return conv.wind_conv(speed,self.units,conv.s_ms)

	def __str__(self):
		return str(self.direction_string + " at " + str(self.toMPH(self.speed)) + " MPH with gusts to " + str(self.toMPH(self.gusts)) + " MPH")

	__repr__ = __str__
