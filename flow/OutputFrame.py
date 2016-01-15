# -*- coding: UTF-8 -*-
'''
the usage grid of wxpython
maybe you could see this link:
http://www.blog.pythonlibrary.org/2010/04/04/wxpython-grid-tips-and-tricks/
'''
import wx
import wx.grid as  gridlib
from LinkSave import LinkSave
class OutputFrame(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Grid with Popup Menu")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(25,8)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,
                       self.showPopupMenu)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND, 5)
        panel.SetSizer(sizer)
        
        linklib = LinkSave()
        lst=linklib.readlines("data")
        rowCount=0
        for s in lst:
        #for number in range(0,10):
            self.grid.AppendRows()
            self.grid.SetCellValue(rowCount,0,s.decode('utf-8'))
            rowCount+=1

    #----------------------------------------------------------------------
    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu
 
        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,"One")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Two")
        menu.Append(self.popupID3, "Three")
 
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()
