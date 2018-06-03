#! /usr/bin/python

import json
import requests

response = requests.get("https://unogs-unogs-v1.p.mashape.com/aaapi.cgi?t=loadvideo&q=tt0486551",
  headers={
    "X-Mashape-Key": "<your key here>",
    "Accept": "application/json"
  }
)
json_data = json.loads(response.text)


country_list = json_data['RESULT']['country']

for c in country_list:
	if 'us' in c['ccode']:
		print "USA OK!"
	else:
		print "Better Luck Next Time"



#clist = c['ccode']

#if 'us' in c['ccode']:
#	print "USA OK!"

#else:
#	print "Better Luck Next Time"

#print(json_data['RESULT']['country']['ccode'])


#print(type(json_data))
#print json_data


