#! /usr/bin/python

from imdbpie import Imdb
imdb = Imdb()

s_result = imdb.search_for_title("Logan")

max_values=len(s_result) 

if max_values > 5:
	max_values=5

for i in xrange(0,max_values,1):
	print s_result[i]


#print s_result[0]

#print(type(dknight))

#print dknight

#print(dknight['imdb_id'])
