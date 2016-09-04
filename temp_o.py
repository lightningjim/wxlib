import conversion as conv
class temp_o(object):

	#Temperature Units
	def __init__(self, temp, units):
		self.temp = temp
		self.units = units

	def toC(self):
		return conv.temp_conv[self.temp,self.units,conv.s_celsius]
		
