import requests
import os
import datetime

token = os.environ.get("SIMONW_TOKEN", "")

response = requests.get('https://api.github.com/users/alx365/repos', auth=('alx365', token))
dates = {}
for i in response.json():
    name = i['name']
    html_url = i['html_url']
    print(name)
    #dates[name] = ''
    releases_url = i['releases_url'].split("{")[0]
    print(releases_url)
    response = requests.get(releases_url, auth=('alx365', token))
    if len(response.json()) > 0:
        if response.json()[0]['draft'] != "true" and len(response.json()[0]['assets']) > 0:
            date = response.json()[0]['assets'][0]['created_at']
            #name = response.json()[0]['assets'][0]['name']
            dates[name] = [date, html_url]
run = 0
for w in sorted(dates, key=dates.get, reverse=True):
    run += 1
    if run < 4:
        print(w + " " + dates[w][0] + "" + dates[w][1])


#dates.sort()
#dates.reverse()
#print(dates)