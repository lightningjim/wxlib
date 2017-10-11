import conversion as conv
class temp(object):

	#Temperature Units
	def __init__(self, temp, units):
		if(units == conv.s_fahrenheit):
			self.temp = conv.temp_conv(temp,units,conv.s_fahrenheit)
		else:
			self.temp = temp
		self.units = conv.s_fahrenheit

	def toF(self):
		return conv.temp_conv(self.temp,self.units,conv.s_fahrenheit)


	def toC(self):
		return conv.temp_conv(self.temp,self.units,conv.s_celsius)

	def toK(self):
		return conv.temp_conv(self.temp,self.units,conv.s_kelvin)

	
	def __str__(self):
		return str(temp)