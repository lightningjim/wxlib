import urllib.request as urllib2
#import csv

#url = "http://mesonet.org/data/basic/mesonet/current/current.csv.txt"
url = "http://www.mesonet.org/data/basic/mesonet/latest/latest.mdf"
wxdata = urllib2.urlopen(url)
for row in wxdata:
	print(row.split())
#	if row[0] == "OKCN":
#		print("Oklahoma City North at " + row[8] + ":" + row[9])
#		print("Temp: " + row[10] + "F")
#		print("Humidity: \n\tDew Point: " + row[11] + "F\n\tRH: " + row[12] + "%")	
#		print("Wind: \n\t" + row[15] + " at " + row[16] + " MPH\n\tgusting to " + row[17] + " MPH")
