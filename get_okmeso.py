#!/usr/bin/python3
import urllib.request as urllib2
import csv
import codecs
import argparse
from mesonet import mesonet

parser = argparse.ArgumentParser(description='Decode Mesonet data')
parser.add_argument('--station',dest='station', default='OKCE', help='Station ID you are looking up')

args = parser.parse_args()

url = "http://www.mesonet.org/data/basic/mesonet/current/current.csv.v4.txt"
response = urllib2.urlopen(url)
wxdata = csv.reader(codecs.iterdecode(response,'utf-8'),delimiter=',')
for row in wxdata:
	# Headers
	if row[0] == "STID":
		print(row)
	if row[0] == args.station:
		print(row)
		test = mesonet(row)
		print(test)