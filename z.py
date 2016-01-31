# -*- coding:utf-8 -*-
import wx
from PythonScriptPanel import PythonScriptPanel
import Utils
from Utils import _
from MongoSave import MongoSave
class BrowserSettingPanel(wx.Panel):
	def __init__(self,parent):  
		wx.Panel.__init__(self, parent, -1,size=wx.DefaultSize, style=wx.WANTS_CHARS, name='MainScrollPanel')  
		self.SetBackgroundColour("green")
		#self.BoxSizer= wx.BoxSizer(wx.VERTICAL)
		
		# #self.SetSizer(self.BoxSizer)
		# box_sizer = wx.WrapSizer(orient=wx.VERTICAL)
		# self.scrolled_window = wx.ScrolledWindow(self,-1)
		# self.scrolled_window.SetBackgroundColour("red")  
		# self.scrolled_window.ShowScrollbars(wx.SHOW_SB_ALWAYS,wx.SHOW_SB_ALWAYS)
		# self.scrolled_window.SetScrollbars(1, 1, 400, 300)  
		# #self.scrolled_window.SetVirtualSize((300, 600))  
		# #self.scrolled_window.SetSize((300,600))
		# self.scrolled_window.SetScrollRate(20, 20)  
	
		# self.scrolled_window.SetSizer(box_sizer)  
		# # for i in range(1, 100	, 1):  
		# # 	box_sizer.Add(wx.StaticText(self.scrolled_window, -1, "ddddd")) 
		# #self.BoxSizer.Add(self.scrolled_window,proportion =1, border = 2,flag = wx.ALL | wx.EXPAND)

		# check = wx.CheckBox(self.scrolled_window,label=_('Open In New Tab'))
		# check.SetValue(True)
		
		# #box_sizer.Add(check) 
		# checkLoadImage = wx.CheckBox(self.scrolled_window,label="load")
		# checkLoadImage.SetValue(True)
		# #box_sizer.Add(checkLoadImage)

		# #box_sizer.Add(BrowserSettingScroll(self))
		# # sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
		# # 	'six', 'seven', 'eight']
		# # wx.StaticText(self.scrolled_window, -1, "Select one:", (15, 15))
		# # cb1 = wx.ComboBox(self.scrolled_window, -1, "zero", (15, 30), wx.DefaultSize,
		# # 	sampleList, wx.CB_DROPDOWN)
		# #box_sizer.Add(cb1)
		# PythonScriptPanel(self.scrolled_window)

	
	def refreshCtrl(self):
		pass
class ScrollBarFrame(wx.Frame):  
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'ScrollBarFrame', size=(800, 450), style=wx.DEFAULT_FRAME_STYLE)  
		self.notebook = wx.Notebook(self, -1, name="notebook")
		self.notebook.SetBackgroundColour("pink")  
		########## 拆分窗口 ##########  
		self.splitter_window = wx.SplitterWindow(self.notebook)
		########## 带滚动的窗体 ##########  
		self.scrolled_window = wx.ScrolledWindow(self.splitter_window, -1)  
		self.scrolled_window.SetBackgroundColour("red")  
		#self.scrolled_window.SetScrollbars(1, 1, 400, 300)  
		self.scrolled_window.SetVirtualSize((1000, 1000))  
		self.scrolled_window.SetScrollRate(20, 20)  
		#self.scrolled_window = ComponentScrollWindow(self.splitter_window)
		#box_sizer = wx.WrapSizer(orient=wx.VERTICAL)  
		box_sizer = wx.BoxSizer(orient=wx.VERTICAL)
		self.scrolled_window.SetSizer(box_sizer)  
		for i in range(1, 100, 1):  
			box_sizer.Add(wx.StaticText(self.scrolled_window, -1, "ddddd"))  

		box_sizer.Add(wx.CheckBox(self.scrolled_window,label=_('Open In New Tab')))

		self.scrolled_window2 = wx.ScrolledWindow(self.splitter_window, -1)  
		self.scrolled_window2.SetBackgroundColour("blue")  
		########## 带滚动的窗体end ##########  
		self.splitter_window.SetMinimumPaneSize(10)  #最小面板大小  
		self.splitter_window.SplitVertically(self.scrolled_window, self.scrolled_window2, 100)  #分割面板  
		self.notebook.AddPage(self.splitter_window, "notebook")  
		save = MongoSave('')
		ret = save.loadDataFile()
# 		str = "{'p2': u'\xa532', 'p1': u'92', 'name': u'\u5c0a\u5b9d\u6bd4\u8428\uff08\u68e0\u4e1c\u5e97\uff09', 'img': u'http://p0.meituan.net/350.214/deal/8dbc10d27257b7530dba82da50b4ba5f105933.jpg', 'rate': u'8189', 'href': u'http://gz.meituan.com/shop/78892#smh:bdw', 'c2': u'\u68e0\u4e0b', 'c1': '\xe7\xbe\x8e\xe9\xa3\x9f'}"

# #{'p2': u'\xa532', 'p1': u'56', 'name': u'\u5c0a\u5b9d\u6bd4\u8428\uff08\u5e7f\u5dde\u5854\u5e97\uff09', 'img': u'http://p0.meituan.net/350.214/deal/a305a189cd2e9f4565749eaa72b7eb29131684.jpg', 'rate': u'5737', 'href': u'http://gz.meituan.com/shop/78898#smh:bdw', 'c2': u'\u5ba2\u6751/\u8d64\u5c97', 'c1': '\xe7\xbe\x8e\xe9\xa3\x9f'}"
# 		str = str.replace("'","\"")
# 		print(str)
# 		j =eval(str)
# 		save.add(j)
class ComponentScrollWindow(wx.ScrolledWindow):
	def __init__(self,parent):
		wx.ScrolledWindow.__init__(self,parent,-1,size = wx.DefaultSize,style = 0,name = "ComponentScrollWindow")		
		self.SetVirtualSize((1000, 1000))  
		self.SetScrollRate(20, 20) 
		self.SetBackgroundColour("yellow")  

class MyApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
		print("__int__")
		print(self)
		
		# i18n support
	def OnExit(self):
		# When app.MainLoop() returns, MessageLoopWork() should
		# not be called anymore.
		print("[wxpython.py] MyApp.OnExit")

if __name__ == '__main__':
	app = MyApp()
	# frame = wx.Frame(parent=None,id=1,title='nn')
	# panel = BrowserSettingPanel(frame)
	frame = ScrollBarFrame()  
	frame.Show()
	app.MainLoop()
	print('main loop finished')
	# Let wx.App destructor do the cleanup before calling
	# cefpython.Shutdown(). This is to ensure reliable CEF shutdown.
	del app
