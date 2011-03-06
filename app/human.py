import urllib,urllib2,cookielib,time
from time import strftime
from cookielib import CookieJar
from urllib2 import HTTPRedirectHandler
from BeautifulSoup import BeautifulSoup

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
		self._getPage("", {
				'jsform': 1,
				'BT': strftime("%H-%M-%S-%m-%d-%Y", time.localtime())
			})

	def _getPage(self, page, params=None):
		"""Get a page"""
		encodedParams = None
		if params is not None:
			encodedParams = urllib.urlencode(params)

		return self._opener.open(self._home + page,
				encodedParams).read()

class HumanClock(HumanPage):
	"""Handles getting the current image from the clock page"""
	_soup = None
	_clockPage = 'clock.php'
	_clockImageName = 'clockImage_main'

	def __init__(self):
		super(HumanClock, self).__init__()

	def GetImageURL(self):
		html = self._getPage(self._clockPage)
		self._soup = BeautifulSoup(html)

		return self._soup.find('img', {'name':self._clockImageName})["src"]

class HumanCalendar(HumanPage):
	pass

if __name__ == '__main__':
	print HumanClock().GetImageURL()
