#!/usr/bin/python3
from datetime import datetime
import pytz
import conversion as conv
from temp import temp as Temp
from wind import wind as Wind
from humidity import humidity as Humidity

class mesonet(object):
	central = pytz.timezone("US/Central")

	def __init__(self, data):
		self.station = data[0]
		self.name = data[1]
		self.location = (data[3],data[4])
		self.observed = datetime(int(data[5]),int(data[6]),int(data[7]),int(data[8]),int(data[9]),0,0, self.central)
		self.air_temp = Temp(float(data[10]), conv.s_fahrenheit)
		self.humidity = Humidity(Temp(float(data[11]),conv.s_fahrenheit), float(data[12]))
		if data[13] == '':
			self.wind_chill = None
		else:
			self.wind_chill = Temp(float(data[13]), conv.s_fahrenheit)
		if data[14] == '':
			self.heat_index = None
		else:
			self.heat_index = Temp(float(data[14]), conv.s_fahrenheit)
		self.wind = Wind(float(data[15]), data[16], float(data[17]), conv.s_mph, float(data[18]))
		#self.wind_dir = (int(data[15]),data[16])
		#self.wind_speed = int(data[17])
		#self.gust = int(data[18])
		self.pressure = float(data[19])


	def getID(self):
		return self.station;

	def __str__(self):
		output = "MESONET\n"
		output += "Station ID: " + self.station + '\n'
		output += "Name: " + self.name + '\n'
		output += "Loc (lat,lon): " + str(self.location) + '\n'
		output += "Observed time: " + self.observed.strftime('%a, %b %d, %Y %I:%M %p') + '\n'
		output += "Air temperature: " + str(self.air_temp.toF()) + "F | " + str(round(self.air_temp.toC(),1)) + "C\n"
		output += "Humidity: " + str(self.humidity) + '\n'
		if self.wind_chill == None:
			output += "Wind chill: None\n"
		else:
			output += "Wind chill: " + str(self.wind_chill) + "F\n"
		if self.heat_index == None:
			output += "Heat index: None\n"
		else:
			output += "Heat index: " + str(self.heat_index) + "F\n"
		output += "Wind: " + str(self.wind) + "\n"
		#output += "Wind: " + str(self.wind_dir) + " at " + str(self.wind_speed) + " MPH\n"
		#output += "Gusts: " + str(self.gust) + " MPH\n"
		output += "Pressure (at sea level): " + str(self.pressure) + " mb"
		return output