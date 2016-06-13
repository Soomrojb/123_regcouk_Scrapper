
import scraperwiki
import lxml.html
import datetime
import urllib2
import requests

today = datetime.date.today()
MySite = 'http://www.dailychanges.com/123-reg.co.uk/';
NewURL = MySite + str(today) + "/"

#html = scraperwiki.scrape(NewURL)
#root = lxml.html.fromstring(html)

qargs = {'Referer':'http://www.dailychanges.com/123-reg.co.uk/2016-06-11/',
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

response = requests.get(NewURL, str(qargs))
root = lxml.html.fromstring(response.content)

print "website loaded successfully"
print str(root)

#html = requests.get(NewURL, str(qargs))
#root = lxml.html.fromstring(str(html.content))
#print str(root)
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

#for loop in range(1,200):
#  elem = root.cssselect("#tab-content-new-domains-tab > div:nth-child(3) > table > tbody > tr:nth-child(6) > td > a")
#  print elem

#print datetime.date.today().strftime("%B %d, %Y")

