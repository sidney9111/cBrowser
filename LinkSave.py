import os
import sys
import struct
from scrapy.selector import HtmlXPathSelector
def ExceptHook(excType, excValue, traceObject):
    import traceback, os, time, codecs
    # This hook does the following: in case of exception write it to
    # the "error.log" file, display it to the console, shutdown CEF
    # and exit application immediately by ignoring "finally" (os._exit()).
    errorMsg = "\n".join(traceback.format_exception(excType, excValue,
        traceObject))
    errorFile = GetApplicationPath("error.log")
    try:
        appEncoding = cefpython.g_applicationSettings["string_encoding"]
    except:
        appEncoding = "utf-8"
    if type(errorMsg) == bytes:
        errorMsg = errorMsg.decode(encoding=appEncoding, errors="replace")
    try:
        with codecs.open(errorFile, mode="a", encoding=appEncoding) as fp:
            fp.write("\n[%s] %s\n" % (time.strftime("%Y-%m-%d %H:%M:%S"), errorMsg))
    except:
        print("[wxpython.py] WARNING: failed writing to error file: %s" % (errorFile))
    # Convert error message to ascii before printing, otherwise
    # you may get error like this:
    # | UnicodeEncodeError: 'charmap' codec can't encode characters
    errorMsg = errorMsg.encode("ascii", errors="replace")
    errorMsg = errorMsg.decode("ascii", errors="replace")
    print("\n"+errorMsg+"\n")
    cefpython.QuitMessageLoop()
    cefpython.Shutdown()
    os._exit(1)

class LinkSave:
    def __int__(self):
        pass
    def save(self,name,string):
        local='links/' + name +'.txt'
        f=open(local,'w')
        f.write(string)
        f.close()
    def load(self,name):
        local='links/' + name + '.txt'
        f=open(local)
        
        self.parse(f.read())
        f.close()
        pass
    def parse(self,string):
        sel = HtmlXPathSelector(text=string)
        #print(string)
        #print(sel.select('//title/text()').extract())
        #print(sel.select('//input').extract())
        inputObjects=sel.select('//input')
        for index, link in enumerate(inputObjects):
            args=(index,link.select('@type').extract())
            for s in link.select('@type').extract():
                print(s)
        pass


if __name__ == '__main__':
    print('[wxpython.py] architecture=%s-bit' % (8 * struct.calcsize("P")))
    #print('[wxpython.py] wx.version=%s' % wx.version())

    # Intercept python exceptions. Exit app immediately when exception
    # happens on any of the threads.
    sys.excepthook = ExceptHook
    link=LinkSave()
    link.load(sys.argv[1])


  