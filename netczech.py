#! /usr/bin/python

from imdbpie import Imdb
import json
import requests

imdb = Imdb()

movie_title = raw_input("Enter movie name:")

s_result = imdb.search_for_title(movie_title)

if len(s_result) == 0:
	print "no movie for you!"
	exit(1)

max_values=len(s_result)

if max_values > 5:
        max_values=5

print "here are your results"

for i in xrange(0,max_values,1):
        output="{index} - {title} {year} ".format(index=i+1,title=s_result[i]['title'], year=s_result[i]['year']) 
	#print s_result[i]
	print output

selection = raw_input("Please enter selection number:")


dknight = s_result[int(selection)-1]



#print(type(dknight))

#print dknight

#print(dknight['imdb_id'])
dbid = (dknight['imdb_id'])

response = requests.get(("https://unogs-unogs-v1.p.mashape.com/aaapi.cgi?t=loadvideo&q=" + dbid),
  headers={
    "X-Mashape-Key": "<your key here>",
    "Accept": "application/json"
  }
)

if len(response.text) == 0:
	print "fuck off"
	exit(1)
#print 'bigdick mofo: {} <<'.format(response.text)

json_data = json.loads(response.text)


country_list = json_data['RESULT']['country']

countries = ""
for c in country_list:
	countries += "|" + c['ccode']

print countries

if 'us' in countries:
	print "USA OK!"
else:
	print "Not available in the U.S."

#        if 'us' in c['ccode']:
#                print "USA OK!"
#        else:
#                print "Better Luck Next Time"

