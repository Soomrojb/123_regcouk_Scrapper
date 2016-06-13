
import scraperwiki
import lxml.html
import datetime
import urllib2

today = datetime.date.today()
MySite = 'http://www.dailychanges.com/123-reg.co.uk/';
NewURL = MySite + str(today) + "/"

#html = scraperwiki.scrape(NewURL)
#root = lxml.html.fromstring(html)

qargs = {'Referer':'http://www.dailychanges.com/123-reg.co.uk/2016-06-11/',
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11}
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive',
       'Referer':'http://www.dailychanges.com/123-reg.co.uk/2016-06-11/'}

urllib2.urlopen(NewURL, qargs)
print "website loaded successfully"

# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

#for loop in range(1,200):
#  elem = root.cssselect("#tab-content-new-domains-tab > div:nth-child(3) > table > tbody > tr:nth-child(6) > td > a")
#  print elem

#print datetime.date.today().strftime("%B %d, %Y")

