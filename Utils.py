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

class FrameRestorerMixin:
    """ Used by top level windows to restore from gidden or iconised state
    and to load and persist window dimensions

    Classes using the mixin must define self.setDefaultDimensions()
    To be able to save, a winConfOption attr must be defined.
    """
    confFile = 'Explorer'
    confSection = 'windowdims'
    frameRestorerWindows = {}

    def restore(self):
        self.Show()
        if self.IsIconized():
            self.Iconize(False)
        self.Raise()

    def setDimensions(self, dims):
        if None in dims:
            if dims[0] is None:
                if dims[1] is not None:
                    self.SetClientSize(tuple(dims[1:]))
            else:
                self.SetPosition(tuple(dims[:-1]))
        else:
            self.SetDimensions(*dims)

    def getDimensions(self):
        pos = self.GetPosition().Get()
        size = self.GetSize().Get()
        return pos + size

    def loadDims(self):
        conf = createAndReadConfig(self.confFile)
        if not conf.has_option(self.confSection, self.winConfOption):
            dims = None
        else:
            dims = eval(conf.get(self.confSection , self.winConfOption),
                        {'wxSize': wx.Size, 'wxPoint': wx.Point,
                         'wxDefaultSize': wx.DefaultSize,
                         'wxDefaultPosition': wx.DefaultPosition,
                         'wx': wx})

        if dims:
            self.setDimensions(dims)
        else:
            self.setDefaultDimensions()

        self.frameRestorerWindows[self.winConfOption] = self

    def saveDims(self, dims=()):
        if dims == ():
            dims = self.getDimensions()
        conf = createAndReadConfig(self.confFile)
        conf.set(self.confSection, self.winConfOption, `dims`)
        writeConfig(conf)

    def restoreDefDims(self):
        self.saveDims(None)
        self.loadDims()
