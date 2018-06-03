#! /usr/bin/python

import unirest
import json

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://unogs-unogs-v1.p.mashape.com/aaapi.cgi?t=loadvideo&q=60029591",
  headers={
    "X-Mashape-Key": "<your key here>",
    "Accept": "application/json"
  }
)

data = response.body()
with open('data.body', 'w') as f:
   body.dump(data, f)

print "all done"



#print response.body


