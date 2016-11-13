###NO SOUP###
import requests, lxml.html
import pandas as pd
import time
from random import random

l=list(range(18))
l.pop(0)
rows = []
start = time.time()
for n in l:
    time.sleep(random.random())
    if n==1:
        url="http://www.yellowpages.com/washington-dc/auto-repair-service"
    else:
        url="http://www.yellowpages.com/washington-dc/auto-repair-service?page=" + str(n)
    response = requests.get(url)

    doc = lxml.html.fromstring(response.content)
    for row in doc.cssselect("div.result"):
        link = row.cssselect("a.business-name")[0].get('href')
        name = row.cssselect("a.business-name")[0].text
        while True:
            try:
                addr = row.cssselect("span.street-address")[0].text
                break
            except IndexError:
                addr = 0
                break
        #addr = row.cssselect("span.street-address")[0].text
        while True:
            try:
                phone = row.cssselect("div.phone.phone.primary")[0].text
                break
            except IndexError:
                phone = 0
                break
        #phone = row.cssselect("div.phone.phone.primary")[0].text
        row = [name,addr,phone,link]
        rows.append(row)
end = time.time()
print "Runtime:", end-start
df = pd.DataFrame(rows, columns=['name','addr','phone','link'])
df
df.to_csv('dc.csv')
