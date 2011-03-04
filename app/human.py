import urllib,urllib2,cookielib,time
from time import strftime
from cookielib import CookieJar
from urllib2 import HTTPRedirectHandler
from BeautifulSoup import BeautifulSoup

CLOCK_IMAGE_NAME = "clockImage_main"

class Human(object):
	"""A class for retrieving "human" content"""
	def __init__(self):
		pass

	def GetCurrentClockURL(self):
		return HumanClock().GetClockURL()

	def GetCurrentCalendar(self):
		pass

class HumanPage(object):
	"""A base class for reading HTML pages"""
	_opener = None
	_page = None
	_home = "http://www.humanclock.com/"

	def __init__(self):
		cookie_handler= urllib2.HTTPCookieProcessor()
		redirect_handler= urllib2.HTTPRedirectHandler()
		self._opener = urllib2.build_opener(redirect_handler, cookie_handler)

		self._navigateHome()

	def _navigateHome(self):
		"""Open the home page to establish necessary cookies"""
		self._opener.open(self._home, urllib.urlencode({'jsform': 1, 'BT': strftime("%H-%M-%S-%m-%d-%Y", time.localtime())}))

	def _getPage(self, page, params=None):
		if self._page is None:
			self._page = self._opener.open(self._home + page).read()
		return self._page

class HumanClock(HumanPage):
	"""Handles getting the current image from the clock page"""
	_soup = None

	def __init__(self):
		super(HumanClock, self).__init__()
		html = self._getPage('clock.php')
		self._soup = BeautifulSoup(html)

	def GetClockURL(self):
		return self._soup.find('img', {'name':CLOCK_IMAGE_NAME})["src"]

class HumanCalendar(HumanPage):
	pass

if __name__ == '__main__':
	print Human().GetCurrentClockURL()
