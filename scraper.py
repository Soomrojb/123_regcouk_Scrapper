
import scraperwiki
import lxml.html
import datetime
#import urllib.request
import urllib2

today = datetime.date.today()
MySite = 'http://www.dailychanges.com/123-reg.co.uk/';
NewURL = MySite + str(today) + "/"

#html = scraperwiki.scrape(NewURL)
#root = lxml.html.fromstring(html)

qargs = {'Referer':'http://www.dailychanges.com/123-reg.co.uk/2016-06-11/', 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}

urllib2.urlopen(NewURL, str(qargs))
print "website loaded successfully"

# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

#for loop in range(1,200):
#  elem = root.cssselect("#tab-content-new-domains-tab > div:nth-child(3) > table > tbody > tr:nth-child(6) > td > a")
#  print elem

#print datetime.date.today().strftime("%B %d, %Y")

