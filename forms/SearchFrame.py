import os, sys
libcef_dll = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        'libcef.dll')
if os.path.exists(libcef_dll):
    # Import a local module
    if (2,7) <= sys.version_info < (2,8):
        import cefpython_py27 as cefpython
    elif (3,4) <= sys.version_info < (3,4):
        import cefpython_py34 as cefpython
    else:
        raise Exception("Unsupported python version: %s" % sys.version)
else:
    # Import an installed package
    from cefpython3 import cefpython
import wx
from LinkSave import LinkSave
class SearchFrame(wx.Frame):
    browser = None
    #mainPanel = None
    def __init__(self, parent,index):
        self.app=parent
        
        title = "wxPython CEF 3 example_"+ str(index)
        wx.Frame.__init__(self, parent=None, id=wx.ID_ANY,
                title=title)
        size=(800,600)
        self.SetPosition((0,0))

        self.SetSize(size)
        
        panel = wx.Panel(self, style=wx.WANTS_CHARS)
        
        #goButton = QtGui.QPushButton("Go", layout)
        #layout.addWidget(self.addressEdit)
        #layout.addWidget(goButton)
        
        button = wx.Button(panel,label="catch",pos=(125,10),size=(50,50))
        #userText = wx.TextCtrl(panel,-1,"Entry your name",size=(175,-1),style=wx.TE_PROCESS_ENTER)

        self.box=wx.BoxSizer(wx.VERTICAL)
        self.top_box=wx.BoxSizer(wx.HORIZONTAL )
        #self.top_box.Add(userText,proportion=5,flag=wx.EXPAND,border=15)
        #create FlexGridSizer
        self.FlexGridSizer=wx.FlexGridSizer( rows=5, cols=5, vgap=5,hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
        #self.FlexGridSizer.Add(button,proportion =0, border = 5,flag = wx.ALL | wx.EXPAND)
        #self.FlexGridSizer.Add(userText,proportion =0, border = 5,flag = wx.ALL | wx.EXPAND)
        #self.top_box.Add(button,proportion=5,flag=wx.EXPAND,border=15)
        

        #self.box.Add(self.top_box,proportion=0,flag=wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT|wx.BOTTOM,border=5)
        #self.box.Add(wx.BoxSizer(wx.VERTICAL),proportion=1,flag=wx.EXPAND)

        #self.box.Add(self.top_box,proportion=1, flag=wx.ALL|wx.EXPAND,border=5)
        #self.box.Add((25,25),proportion=1)
        #panel.SetSizerAndFit(self.box)

        self.BoxSizer=wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizerAndFit(self.FlexGridSizer)
        self.MPL= wx.Panel(self, style=wx.WANTS_CHARS)
        box=wx.BoxSizer(wx.HORIZONTAL)
        self.userTextT2 = wx.TextCtrl(self.MPL,-1,"www.baidu.com",size=(1,28),style=wx.TE_PROCESS_ENTER)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnButton, self.userTextT2)
        self.buttonT2=wx.Button(self.MPL,label="Go!",size=(1,28))
        self.MPL.SetSizer(box)
        box.Add(self.userTextT2,proportion=7.13,border=5,flag=wx.ALL)
        box.Add(self.buttonT2,proportion=2.84,border=5,flag=wx.ALL)
        self.MPL.Centre(wx.BOTH)

        self.BoxSizer.Add(self.MPL,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(panel,proportion =0, border = 0,flag = wx.ALL | wx.EXPAND)
    
        self.SetSizer(self.BoxSizer)
        
        panel.Bind(wx.EVT_SIZE, self.OnSize)
        #self.Bind(wx.EVT_BUTTON, self.OnButton, self.buttonT2)
        self.Bind(wx.EVT_BUTTON, lambda evt, mark=self,control=self.userTextT2 : self.app.OnSearchButton(evt,mark,control), self.buttonT2)
        self.Bind(wx.EVT_OPEN,self.OnOpen)
        self.CreateMenu()
    def OnSize(self, event):
        print('on size')
        cefpython.WindowUtils.OnSize(self.GetHandle(), 0, 0, 0)
    def OnButton(self,evt):
        # frame = MainFrame(url=self.userTextT2.GetValue(),pos=self.GetPosition())
        # frame.Show()
        # self.app.GetTopWindow().Close()
        link=LinkSave()
        link.save('a_1','dfasdfds')
    def OnClose(self, event):

        pass
    def CreateMenu(self):       
        menubar = wx.MenuBar() 
        preferencesMenu = wx.Menu()
        munCapture = preferencesMenu.AppendCheckItem(4,"Capture Sebsite")
        preferencesMenu.Check(4,True)
        self.Bind(wx.EVT_MENU,self.OnSelectCapture,munCapture)
        
        menubar.Append(preferencesMenu,"&Preferences")
        
        self.SetMenuBar(menubar)
    def OnSelectCapture(self,event):
        pass