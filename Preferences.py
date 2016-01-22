import sys,os
import wx
if hasattr(sys, "frozen"):
    pyPath = os.path.abspath(os.path.dirname(sys.executable))
else:
    pyPath = os.path.abspath(os.path.dirname(__file__))

i18nLanguage = wx.LANGUAGE_DEFAULT