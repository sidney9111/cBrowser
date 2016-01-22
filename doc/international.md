# How to displays by different  country or culture
http://zetcode.com/wxpython/in18/

## Generate po files
...
## Initial locale as earlier
It's should be init in ==OnInit== function earlier. OnInit() > __init__(self)

```python
import wx
class MyApp:
    def __init__(self):
        pass
    def OnInit(self):
        self.locale = wx.Locale(Preferences.i18nLanguage)
        wx.Locale.AddCatalogLookupPathPrefix(os.path.join(Preferences.pyPath, 'locale'))
        # if hasattr(sys, 'frozen'):
        #     self.locale.AddCatalog('wxstd')
        self.locale.AddCatalog('boa') 

```
