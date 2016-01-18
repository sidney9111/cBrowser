# -*- coding: UTF-8 -*-
import wx
class MainScrollPanel(wx.Panel):  
    def __init__(self,parent):  
        wx.Panel.__init__(self, parent, -1,size=wx.DefaultSize, style=wx.WANTS_CHARS, name='MainScrollPanel')  
        self.SetBackgroundColour("green")
        #self.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))  #鼠标形状  
  
  
        ########## 窗体底部状态栏 ##########  
        # self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)  
        # self.statusbar.SetStatusText(u"frame-Helloworld", 0)  
        # self.statusbar.SetStatusText(u"HelloHello!", 1)  
  
        # self.notebook = wx.Notebook(self, -1, name="notebook")  
        # self.notebook.SetBackgroundColour("pink")  
  
        ########## 拆分窗口 ##########  
        

        self.splitter_window = wx.SplitterWindow(self)  
        #self.splitter_window.SetSize((500, 600)) 

        topBoxSizer=wx.BoxSizer(wx.HORIZONTAL)
        '''
#proportion参数定义了构件在既定方向上所占空间的比例，是相对的，相对于其他组件
        '''
        '''
#The wxALIGN_* flags allow you to specify the alignment of the item within the space allotted to it by the sizer, adjusted for the border if any.
wxALIGN_CENTER
wxALIGN_CENTRE
wxALIGN_LEFT
wxALIGN_RIGHT
wxALIGN_TOP
wxALIGN_BOTTOM
wxALIGN_CENTER_VERTICAL
wxALIGN_CENTRE_VERTICAL
wxALIGN_CENTER_HORIZONTAL
wxALIGN_CENTRE_HORIZONTAL
        '''
        '''
#These flags are used to specify which side(s) of the sizer item the border width will apply to.
wxTOP
wxBOTTOM
wxLEFT
wxRIGHT
wxALL
        '''
        topBoxSizer.Add(self.splitter_window,proportion=2,border=wx.ALIGN_TOP,flag=wx.RIGHT)
        topBoxSizer.SetMinSize(wx.Size(100,200))
        #topBoxSizer.Add(goButton,proportion=2,border=5,flag=wx.ALL)
        self.SetSizer(topBoxSizer)
        ########## 带滚动的窗体 ##########  
        # self.scrolled_window = wx.ScrolledWindow(self.splitter_window, -1)  
        # self.scrolled_window.SetBackgroundColour("red")  
        # #self.scrolled_window.SetScrollbars(1, 1, 400, 300)  
        # self.scrolled_window.SetVirtualSize((300, 600))  
        # self.scrolled_window.SetScrollRate(20, 20)  
  
        # box_sizer = wx.WrapSizer(orient=wx.VERTICAL)  
        # self.scrolled_window.SetSizer(box_sizer)  
        # for i in range(1, 100, 1):  
        #     box_sizer.Add(wx.StaticText(self.scrolled_window, -1, "ddddd"))  
    
        self.pages = wx.Notebook(id=1, name='pages',
              parent=self.splitter_window, 
              style=0)
        self.mainPanel = wx.Panel(self.pages, style=wx.WANTS_CHARS)
        self.pages.AddPage(imageId=-1, page=self.mainPanel, select=True, text=u'b2')
        #self.BoxSizer.Add(pages,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)

        # self.scrolled_window2 = wx.ScrolledWindow(self.splitter_window, -1)  
        # self.scrolled_window2.SetBackgroundColour("red")  

        ########## 带滚动的窗体end ##########  
        self.scrolled_window = wx.Panel(self.splitter_window)
        #self.scrolled_window.SetSizer(topBoxSizer)
        #self.scrolled_window.SetBackgroundColour("blue")
        #goButton=wx.Button(self.scrolled_window,label="Go!",size=(50,28))
        check = wx.CheckBox(self.scrolled_window,label="在新窗口打开页面")
        check.SetValue(True)

        checkLoadImage = wx.CheckBox(self.scrolled_window,label="加载页面图片",pos=wx.Point(0,100))
        checkLoadImage.SetValue(True)

        # self.scrolled_window2 =wx.Panel(self.splitter_window)
        # self.scrolled_window2.SetBackgroundColour("red")
        self.splitter_window.SetMinimumPaneSize(10)  #最小面板大小  
        self.splitter_window.SplitVertically(self.scrolled_window, self.pages, 100)  #分割面板  
        #self.notebook.AddPage(self.splitter_window, "notebook")  
