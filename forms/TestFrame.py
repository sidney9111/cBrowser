import wx
from LinkSave import LinkSave
import re
class TestFrame(wx.Frame):
    visitor = None
    #mainPanel = None
    def __init__(self):
    	title = "TestFrame"
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title=title)
        size=(800,600)
    def load(self, frame):
    	self.visitor=Visitor()
    	
    	urlString=frame.GetUrl()
    	urlString=urlString.replace('?','%3F')
    	urlString=urlString.replace('/','%2F')
    	urlString=urlString.replace(' ','%20')
    	urlString=urlString.replace('+','%2B')
    	urlString=urlString.replace(':','%2A')
    
    	self.visitor.url=urlString
    	frame.GetSource(self.visitor)
class Visitor:
    def Visit(self, string):
    	link=LinkSave()
    	link.save(self.url,string)
        print("[TestFrame.py] saved file="+urlString)
