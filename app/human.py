import urllib,urllib2,cookielib
from cookielib import CookieJar
from urllib2 import HTTPRedirectHandler
from BeautifulSoup import BeautifulSoup

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
	_opener = None
	_home = "http://www.humanclock.com/"

	def __init__(self):
		cookie_handler= urllib2.HTTPCookieProcessor()
		redirect_handler= urllib2.HTTPRedirectHandler()
		self._opener = urllib2.build_opener(redirect_handler, cookie_handler)

		self._navigateHome()

	def _navigateHome(self):
		"""Open the home page to establish necessary cookies"""
		self._opener.open(self._home)

	def _getPage(self, page, params=None):
		return self._opener.open(self._home + page).read()

class HumanClock(HumanPage):
	"""Handles getting the current image from the clock page"""
	def __init__(self):
		super(HumanClock, self).__init__()

	def getImage(self):
		html = self._getPage('clock.php')

		soup = BeautifulSoup(html)
		return soup.findAll('img', {'name':'locationimage'})

class HumanCalendar(HumanPage):
	pass

if __name__ == '__main__':
	Human().getCurrentClock()
