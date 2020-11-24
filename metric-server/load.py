import requests
import time

url = 'http://ab1fc4b15074611eab92412a25270fca-671953508.us-east-1.elb.amazonaws.com'
url_metrics = 'http://ab1fc4b15074611eab92412a25270fca-671953508.us-east-1.elb.amazonaws.com/metrics'
url_health = 'http://ab1fc4b15074611eab92412a25270fca-671953508.us-east-1.elb.amazonaws.com/health'

while True:
    payload = ""
    #payload = open("request.json")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.get(url, data=payload, headers=headers)
    print r.text
    time.sleep(1)
    r = requests.get(url_metrics, data=payload, headers=headers)
    print r.text
    time.sleep(2)
    r = requests.get(url_health, data=payload, headers=headers)
    print r.text
    time.sleep(3)
    
