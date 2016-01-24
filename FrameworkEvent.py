import wx
class FrameworkEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):                   
        wx.PyCommandEvent.__init__(self, evtType, id)  
        self.eventArgs = ""  
    def GetEventArgs(self):   
        return self.eventArgs   
    def SetEventArgs(self, args):   
        self.eventArgs = args   