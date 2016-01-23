from Utils import Singleton
import time
class FlowManagement(Singleton):
	def __init__(self,browser=None):
		if (browser!=None):
			self.browser = browser
		self.url = ""
	def LoadUrl(self,url):
		self.browser.LoadUrl(url)
		self.url = url
		time.sleep(3)
	def _OnLoadEnd(self):
		if (self.url ==""):
			return
		if (self.browser.GetMainFrame().GetUrl()==self.url):
			self.url = ""