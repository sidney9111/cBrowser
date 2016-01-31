import wx
wxID_EVTCATS = wx.NewId()
import Utils
class MonitorFrame(wx.Frame,Utils.FrameRestorerMixin):
	def __init__(self):
		wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title='Monitor')
		size=(800,600)
		self.categoryClasses = wx.ListCtrl(self, wxID_EVTCATS, style=wx.LC_LIST)
		
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
	def Clear(self):
		self.categoryClasses.ClearAll()
	def Log(self,string):
		self.categoryClasses.InsertStringItem(0,string)
	def OnCloseWindow(self,event):
		self.Show(False)
	def restore(self):
		Utils.FrameRestorerMixin.restore(self)   