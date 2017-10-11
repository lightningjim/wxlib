#!/usr/bin/python3
import urllib.request as urllib2
import csv
import codecs
import argparse
from mesonet import mesonet as Mesonet

test = Mesonet("NRMN")
print(test)