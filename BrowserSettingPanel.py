import wx
from PythonScriptPanel import PythonScriptPanel
import Utils
from Utils import _
class BrowserSettingPanel(wx.Panel):
	def __init__(self,parent,name="aa"):  
		print("BrowserSettingPanel param testing ",name)
		print("BrowserSettingPanel param testing ",parent)
		wx.Panel.__init__(self, parent, -1,size=wx.DefaultSize, style=wx.WANTS_CHARS, name='MainScrollPanel')  
		self.SetBackgroundColour("green")
		#self.BoxSizer= wx.BoxSizer(wx.VERTICAL)
		
		#self.SetSizer(self.BoxSizer)
		box_sizer = wx.WrapSizer(orient=wx.VERTICAL)
		self.scrolled_window = wx.ScrolledWindow(self,-1)
		self.scrolled_window.SetBackgroundColour("red")  
		self.scrolled_window.ShowScrollbars(wx.SHOW_SB_ALWAYS,wx.SHOW_SB_ALWAYS)
		self.scrolled_window.SetScrollbars(1, 1, 400, 300)  
		self.scrolled_window.SetVirtualSize((300, 600))  
		self.scrolled_window.SetSize((300,600))
		self.scrolled_window.SetScrollRate(20, 20)  
	
		self.scrolled_window.SetSizer(box_sizer)  
		# for i in range(1, 100	, 1):  
		# 	box_sizer.Add(wx.StaticText(self.scrolled_window, -1, "ddddd")) 
		#self.BoxSizer.Add(self.scrolled_window,proportion =1, border = 2,flag = wx.ALL | wx.EXPAND)

		check = wx.CheckBox(self.scrolled_window,label=_('Open In New Tab'))
		check.SetValue(True)
		
		#box_sizer.Add(check) 
		checkLoadImage = wx.CheckBox(self.scrolled_window,label="load")
		checkLoadImage.SetValue(True)
		#box_sizer.Add(checkLoadImage)

		#box_sizer.Add(BrowserSettingScroll(self))
		# sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
		# 	'six', 'seven', 'eight']
		# wx.StaticText(self.scrolled_window, -1, "Select one:", (15, 15))
		# cb1 = wx.ComboBox(self.scrolled_window, -1, "zero", (15, 30), wx.DefaultSize,
		# 	sampleList, wx.CB_DROPDOWN)
		#box_sizer.Add(cb1)
		PythonScriptPanel(self.scrolled_window)
	def refreshCtrl(self):
		pass