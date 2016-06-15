import requests
import scraperwiki
import lxml.html
from BeautifulSoup import BeautifulSoup
from lxml import etree

site = 'http://www.dailychanges.com/123-reg.co.uk/'
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate, sdch',
           'Accept-Language':'en-US,en;q=0.8',
           'Cache-Control':'max-age=0',
           'Connection':'keep-alive',
           'Host':'www.dailychanges.com',
           'If-Modified-Since':'Mon, 13 Jun 2016 20:38:04 GMT',
           'Upgrade-Insecure-Requests':'1',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'}


response = requests.get(site, headers=headers)
soup = BeautifulSoup(response.content)

# print soup.find('a')
print soup

