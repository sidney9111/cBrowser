import wx
class PythonScriptPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1,size=(300,300), style=wx.WANTS_CHARS, name='PythonScriptPanel')  
		
		wx.StaticText(self, -1, "Select one:", (15, 15))
		sampleList = ['onLoaded',""]
		wx.ComboBox(self, -1, "", (15, 30), wx.DefaultSize,  
			sampleList, wx.CB_DROPDOWN)  
		
		scriptLabel=wx.StaticText(self,-1,"script:",pos=(15,55))
		scriptText=wx.TextCtrl(self,-1,'meituan.py',pos=(35,55),size=(175,-1),style=wx.TE_READONLY)






