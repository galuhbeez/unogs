#! /usr/bin/python

from imdbpie import Imdb
import json
import requests

imdb = Imdb()


#get the movie title to search and limit results 6>
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
	print output

selection = raw_input("Please enter selection number:")

t_search = s_result[int(selection)-1]


#use the imdb_id search result to get the list of countries title is available
dbid = (t_search['imdb_id'])

response = requests.get(("https://unogs-unogs-v1.p.mashape.com/aaapi.cgi?t=loadvideo&q=" + dbid),
  headers={
    "X-Mashape-Key": "",
    "Accept": "application/json"
  }
)

if len(response.text) == 0:
	print "fuck off"
	exit(1)

json_data = json.loads(response.text)

country_list = json_data['RESULT']['country']

countries = ""
for c in country_list:
	countries += "|" + c['ccode']

print countries

#check if available in the us
if 'us' in countries:
	print "USA OK!"
else:
	print "Not available in the U.S."
