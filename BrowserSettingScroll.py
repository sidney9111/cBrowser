'''
this is a wx control testing page
could be execute directly on console as BrowserSettingScroll.py
'''
import wx
class BrowserSettingScroll(wx.Frame):
     
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Combo Box Example', 
                size=(350, 300))
        panel = wx.Panel(self, -1)
        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']
        wx.StaticText(panel, -1, "Select one:", (15, 15))
        cb1 = wx.ComboBox(panel, -1, "zero", (15, 30), wx.DefaultSize,
                    sampleList, wx.CB_DROPDOWN)
        cb2 = wx.ComboBox(panel, -1, "zero", (150, 30),(200,5),
                        sampleList, wx.CB_SIMPLE | wx.CB_SORT)
        # self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, cb1)
        # self.Bind(wx.EVT_TEXT, self.EvtText, cb1)
        # cb1.Bind(wx.EVT_TEXT_ENTER, self.EvtTextEnter)
        # cb1.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        # cb1.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
 
         
    def EvtComboBox(self, evt):
        cb = evt.GetEventObject()
        print evt.GetSelection()
        #print('EvtComboBox: %s\nClientData: %s\n' % (evt.GetString(), data))
 
    def EvtText(self, evt):
        print('EvtText: %s\n' % evt.GetString())
        wx.MessageBox("aaa")
        evt.Skip()
 
    def EvtTextEnter(self, evt):
        print('EvtTextEnter: %s' % evt.GetString())
        evt.Skip()
         
    def OnSetFocus(self, evt):
        print "OnSetFocus"
        evt.Skip()
 
    def OnKillFocus(self, evt):
        print "OnKillFocus"
                         
if __name__ == '__main__':
    app = wx.PySimpleApp()
    BrowserSettingScroll().Show()
    app.MainLoop()    