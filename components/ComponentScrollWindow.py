import wx
class ComponentScrollWindow(wx.ScrolledWindow):
	def __init__(self,parent):  
		wx.ScrolledWindow.__init__(self, parent, -1,size=wx.DefaultSize, name='ComponentScrollWindow')  
		self.SetBackgroundColour("yellow")
		#box_sizer = wx.WrapSizer(orient=wx.VERTICAL)
		box_sizer = wx.BoxSizer(orient=wx.VERTICAL)
		self.SetVirtualSize((300, 600))  
		#self.scrolled_window.SetSize((300,600))
		self.SetScrollRate(20, 20)  
	
		self.SetSizer(box_sizer)  
		self.box_sizer = box_sizer
	def Add(self,ctrl):
		self.box_sizer.Add(ctrl)
