# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import scraperwiki
import lxml.html
import datetime
import urllib

today = datetime.date.today()
MySite = 'http://www.dailychanges.com/123-reg.co.uk/';
NewURL = MySite + str(today) + "/"

#html = scraperwiki.scrape(NewURL)
#root = lxml.html.fromstring(html)

urllib.open(NewUrl)

# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")

#for loop in range(1,200):
#  elem = root.cssselect("#tab-content-new-domains-tab > div:nth-child(3) > table > tbody > tr:nth-child(6) > td > a")
#  print elem

#print datetime.date.today().strftime("%B %d, %Y")

