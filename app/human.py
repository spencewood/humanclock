import urllib,urllib2,cookielib
from BeautifulSoup import BeautifulSoup

#User agent that will access the pages
PEOPLE_USER_AGENT = { 'User-agent': 'Boxee Python Agent' }

class Human(object):
	"""A class for retrieving "human" content"""
	def __init__(self):
		pass

	def getCurrentClock(self):
		HumanClock().getImage()

	def getCurrentCalendar(self):
		pass

class HumanPage(object):
	"""A base class for reading HTML pages"""
	def _getPage(self, page_url, params=None):
		encoded_params = None
		if params:
			encoded_params = urllib.urlencode(params)
		
		source = urllib2.urlopen(page_url)

		return source.read()

class HumanClock(HumanPage):
	"""Handles getting the current image from the clock page"""
	def __init__(self):
		pass

	def getImage(self):
		html = self._getPage('http://www.humanclock.com/clock.php')

		soup = BeautifulSoup(html)
		assert False, soup.findAll('img')

class HumanCalendar(HumanPage):
	pass

if __name__ == '__main__':
	Human().getCurrentClock()
