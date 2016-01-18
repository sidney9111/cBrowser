# -*- coding: UTF-8 -*-
import wx
class BrowserSettingPanel(wx.Panel):
	def __init__(self,parent):  
		wx.Panel.__init__(self, parent, -1,size=wx.DefaultSize, style=wx.WANTS_CHARS, name='MainScrollPanel')  
		self.SetBackgroundColour("green")
		check = wx.CheckBox(self,label="在新窗口打开页面")
		check.SetValue(True)
		checkLoadImage = wx.CheckBox(self,label="加载页面图片",pos=wx.Point(0,100))
		checkLoadImage.SetValue(True)
	def refreshCtrl(self):
		pass