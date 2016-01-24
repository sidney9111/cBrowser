import wx
_ = wx.GetTranslation

class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  

class Singleton2(type):
 
  def __init__(cls, name, bases, dict):
    super(Singleton2, cls).__init__(name, bases, dict)
    cls._instance = None
 
  def __call__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(Singleton2, cls).__call__(*args, **kwargs)
    return cls._instance
