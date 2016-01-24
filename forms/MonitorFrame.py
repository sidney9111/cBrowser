import wx
wxID_EVTCATS = wx.NewId()
class MonitorFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title='Log')
		size=(800,600)
		self.categoryClasses = wx.ListCtrl(self, wxID_EVTCATS, style=wx.LC_LIST)
		for i in range(1,10):
			self.categoryClasses.InsertStringItem(0, 'ttt')
	def Clear(self):
		self.categoryClasses.ClearAll()
	def Log(self,string):
		self.categoryClasses.InsertStringItem(0,string)