from Utils import Singleton
import time
from FrameworkEvent import FrameworkEvent
import wx
class FlowManagement(Singleton):
	'''
	Because FlowManagement is Singleton
	For multiplue programmer development,the parent param should be seldom inited 
	'''
	def __init__(self,parent=None):
		if (parent!=None and hasattr(self,'parent')==False):
			self.parent = parent
		self.url = ""
		#self.EVT_TYPE = evt
	def SetEventID(self,id):
		self.EVT_TYPE = id
	def LoadUrl(self,url):
		self.parent.browser.LoadUrl(url)
		print('flow manager load url111111111111111111111111111')
		print(self.EVT_TYPE)
		evt = FrameworkEvent(self.EVT_TYPE,1)
		evt.SetEventArgs(url)
		self.parent.GetEventHandler().ProcessEvent(evt)
		self.url = url	
	def GetBrowser():
		return self.parent.browser
	def _OnLoadEnd(self):
		if (self.url ==""):
			return
		if (self.parent.browser.GetMainFrame().GetUrl()==self.url):
			self.url = ""
	def CheckIsLoading(self):
		if (self.url==""):
			return False
		else:
			return True
	def ExecuteJavascript(self,js):
		print("FlowManagement++++")
		print("FlowManagement++++")
		print("FlowManagement++++ javascript")
		self.parent.browser.GetMainFrame().ExecuteJavascript(js)