#import urllib3
#from bs4 import BeautifulSoup

#http = urllib3.PoolManager()
#RESPONSE = http.request('GET', 'https://authoraditiagarwal.com')
#soup = BeautifulSoup(RESPONSE.data, 'lxml')
#soup = soup.text
#id = soup.findAll("span", {"class": "tmax"})

#print(id.text)

import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://family.axioscloud.it/Secret/REFamily.aspx")
r = bs(r.text,'lxml')
votes = r.findAll("td")
print(votes)
