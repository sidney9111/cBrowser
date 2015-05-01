# -*- coding:utf-8 -*-  
import time
import wx
import logging
import logging.config
from RepeatableTimer import RepeatableTimer
from scrapy.selector import HtmlXPathSelector
import sys
sys.path.append("robot")
from Meitu import Meitu
from threading import Thread
#define notification event for thread completion
EVT_RESULT_ID=wx.NewId()
def EVT_RESULT(win,func):
	win.Connect(-1,-1,EVT_RESULT_ID,func)
class ResultEvent(wx.PyEvent):
	def __init__(self,data):
		wx.PyEvent.__init__(self)
		self.SetEventType(EVT_RESULT_ID)
		self.data=data
class LoopThread(Thread):
	def __init__(self, wxObject):
		Thread.__init__(self)
		self.wxObject=wxObject
		self.start()
	def run(self):
		meitu=Meitu(self)
		meitu.loop("http://auction.jd.com/9994009")
		#meitu.loop("http://www.meitu.com")

	def ended(self):
		wx.PostEvent(self.wxObject, ResultEvent(1))
class LogFrame(wx.Frame):
	def __init__(self,parent):
		title = "LogFrame_" + str(parent.main.getIndex())

		self.parent=parent
		wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title=title)
		size=(800,600)
		self.l=1
		logging.config.fileConfig("./logging.conf")    # 采用配置文件  
		# create logger  
		self.logger = logging.getLogger("simple")  

		panel = wx.Panel(self, style=wx.WANTS_CHARS)
		button = wx.Button(panel,label="load",pos=(125,10),size=(50,50))
		self.Bind(wx.EVT_BUTTON, self.OnButton, button)
		
		EVT_RESULT(self,self.update)

	def update(self,msg):
		self.logger.debug("update ended........")
	def start(self):
		self.parent.main.getBrowser().LoadUrl("http://www.meitu.com/choose/m2")
	def OnButton(self,event):
		print("OnButton")
		self.url="http://auction.jd.com/9994009"
		self.logger.debug(self.url)
		#self.parent.main.getBrowser().LoadUrl(self.url)
		LoopThread(self)
	def read(self,frame):
		self.visitor=Visitor()
		frame.GetSource(self.visitor)
		self.logger.debug("read str.....")
		if self.l==1:
			t=RepeatableTimer(2,self.loop)
			t.start()
		print("read"+str(self.l))
	def loop(self):
		print("loop")

		#url=self.parent.mainBrowser.getMainFrame().GetUrl()
		self.parent.main.getBrowser().Reload()
class Visitor:
    def Visit(self, string):
		#print("[LogFrame.py] string"+string)
		self.parse(string)
		pass