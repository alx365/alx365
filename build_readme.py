import requests
import os
import datetime

token = os.environ.get("SIMONW_TOKEN", "")
#print(token)
response = requests.get('https://api.github.com/users/alx365/repos',
    auth=('alx365', token)
    #headers={"Authorization": "token" + token}
    )
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
injection_text = "### Latest releases:"
for w in sorted(dates, key=dates.get, reverse=True):
    run += 1
    if run < 4:
        print(w + " " + dates[w][0] + " " + dates[w][1])
        
        injection_text = injection_text + "\n "+ str(run) + " . [" + w +"]("+dates[w][1]+"): " + dates[w][0]
        
        
#print(injection_text)
f = open('README_prefab.md')
text = f.read().replace("///////////////////////////AUTOMATIC CONTENT GOES HERE///////////////////////////", injection_text)
print("File: " + text)

readme = open("README.md", "w+")
readme.write(text)
#dates.sort()
#dates.reverse()
#print(dates)