# -*- coding: UTF-8 -*-
import wx
from PythonScriptPanel import PythonScriptPanel
class BrowserSettingPanel(wx.Panel):
	def __init__(self,parent):  
		wx.Panel.__init__(self, parent, -1,size=wx.DefaultSize, style=wx.WANTS_CHARS, name='MainScrollPanel')  
		self.SetBackgroundColour("green")
	
		'''
		BoxSizer 布局管理
参数说明：
orient：wx.VERTICAL（垂直方向） 或 wx.HORIZONTAL（水平方向）
proportion：控件在方向上所占空间的相对于其他组件比例，
porportion=0，表示保持本身大小；
porportion=1，表示在水平方向上占三分之一的空间；
porportion=2，表示在水平方向上占三分之二的空间。
flag： wx.TOP | wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.ALL | 
wx.EXPAND（自动填充）'''
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

		check = wx.CheckBox(self.scrolled_window,label="在新窗口打开页面")
		check.SetValue(True)
		
		#box_sizer.Add(check) 
		checkLoadImage = wx.CheckBox(self.scrolled_window,label="加载页面图片")
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