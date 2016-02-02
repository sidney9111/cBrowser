from Utils import Singleton
import time
from FrameworkEvent import FrameworkEvent
import wx
import thread
import os
libcef_dll = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'libcef.dll')
if os.path.exists(libcef_dll):
    # Import a local module
    if (2,7) <= sys.version_info < (2,8):
        import cefpython_py27 as cefpython
    elif (3,4) <= sys.version_info < (3,4):
        import cefpython_py34 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
else:
    # Import an installed package
    from cefpython3 import cefpython
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
		print('flow manager load url33333333333333333')
		print(self.EVT_TYPE)
		evt = FrameworkEvent(self.EVT_TYPE,1)
		evt.SetEventArgs(url)
		self.parent.GetEventHandler().ProcessEvent(evt)
		self.url = url	
	def GetBrowser(self):
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
		self.source = SourceVisitor()
		self.parent.browser.GetMainFrame().GetSource(self.source)
		print("FlowManagement url=",self.parent.browser.GetMainFrame().GetUrl())
	def TestPythonCallback(self,url=""):
		#jsCallback.Call(self.PyCallback)
		print("[FlowManagement.py] finsish js call back")
		self.lock = False
		self.lockargs = url
	def PyCallback(self, *args):
		message = "PyCallback() was executed successfully! "\
			"Arguments: %s" % str(args)
		print("[FlowManagement.py] "+message)
		#self.mainBrowser.GetMainFrame().ExecuteJavascript("window.alert(\"%s\")" % message)
	def Lock(self):
		print("[FlowManagement.py] lock")
		for v in cefpython.JavascriptBindings.__dict__:
			print(v)
		jsBindings = cefpython.JavascriptBindings(bindToFrames=True, bindToPopups=False)
		jsBindings.SetObject("exmanager",self)
		self.parent.browser.SetJavascriptBindings(jsBindings)
		self.lock = True
class SourceVisitor:
	def Visit(self,string):
		print("FlowManagement string visit")
		from LinkSave import LinkSave
		save = LinkSave()
		save.save("temp",string)

