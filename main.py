from datetime import datetime
import json
import requests
import urllib
import urllib2




def post_data(output,value):
    endpoint_url='Sumo_Logic_END_POINT_HERE'
    output['RT']=value
    #output['URL']=modurl 
    #output['Ccontroller']=modcontroller
    header = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)"}
    values = urllib.urlencode(output)
    request = urllib2.Request(endpoint_url, values.replace('&',' '), header)
    #try:
    response = urllib2.urlopen(request, timeout=1)


def lambda_handler(event,context):
  url = "https://api.uptimerobot.com/v2/getMonitors"
  payload = "api_key=YOUR_API_KEY&format=json&logs=1&response_times=1"
  headers = {'content-type': "application/x-www-form-urlencoded",'cache-control': "no-cache"}
  response = requests.request("POST", url, data=payload, headers=headers)
  output=response.text
  json_data = json.loads(output)
  monitor = (json_data['monitors'])
  mon_dc=(monitor[0])
  response_time=mon_dc["response_times"]  # response_time is a list with dict as an index

  dictonary={}
  for x in response_time:
   va=x['value']
   post_data(dictonary,va)
