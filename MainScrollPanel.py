# -*- coding: UTF-8 -*-
import wx
class MainScrollPanel(wx.Panel):  
    def __init__(self,parent):  
        wx.Panel.__init__(self, parent, -1,pos=wx.DefaultPosition,size=wx.Size(100,100), style=wx.WANTS_CHARS, name='MainScrollPanel')  
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
        self.splitter_window.SetSize((500, 600)) 
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
  
        # self.scrolled_window2 = wx.ScrolledWindow(self.splitter_window, -1)  
        # self.scrolled_window2.SetBackgroundColour("blue")  
        ########## 带滚动的窗体end ##########  
        self.scrolled_window = wx.Panel(self.splitter_window)
        self.scrolled_window.SetBackgroundColour("blue")
        self.scrolled_window2 =wx.Panel(self.splitter_window)
        self.scrolled_window2.SetBackgroundColour("red")
        self.splitter_window.SetMinimumPaneSize(100)  #最小面板大小  
        self.splitter_window.SplitVertically(self.scrolled_window, self.scrolled_window2, 100)  #分割面板  
        #self.notebook.AddPage(self.splitter_window, "notebook")  
