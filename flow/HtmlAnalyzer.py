# -*- coding: UTF-8 -*-
#import os
#import sys
import struct
from scrapy.selector import HtmlXPathSelector
import FlowConst
from LinkSave import LinkSave
##from scrapy.selector import Selector #scrapy 1.1 api
'''
Scrapy:An open source and collaborative framework for extracting the data you need from websites.
Documentation:http://scrapy.org/doc/
Remark:need proxy to fanqiang, and this code is base on version 0.14
'''
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
data_lst = []
class HtmlAnalyzer:
    def __int__(self):
        pass

    def parse(self,string):
        sel = HtmlXPathSelector(text=string)
        #print(string)
        #print(sel.select('//title/text()').extract())
        #print(sel.select('//input').extract())
        #case 1
        # inputObjects=sel.select('//input')
        # for index, link in enumerate(inputObjects):
        #     args=(index,link.select('@type').extract())
        #     for s in link.select('@type').extract():
        #         print(s)
        # pass
        #case 2
        # inputObjects=sel.select('//a')
        # for index,a in enumerate(inputObjects):
        #     print(a.extract())
        
        #case 3
        # inputObjects=sel.select('//div[@class="mod-picList"]/div/h3/a/@href')
        # for i,href in enumerate(inputObjects):
        #     print(href.extract())
        linkSave = LinkSave()
        reload(FlowConst)
        lst = FlowConst.Read(sel)

        if(lst):
            # ret = self.RepeatCheck(lst)
            # if(ret==False):
            for key,value in enumerate(lst):
                linkSave.add("data",value)
                print(value)
        data_lst = lst
    #某些原因chrome embed会读取多次
    def RepeatCheck(self,lst):#1行单字段
        if(len(data_lst)!=len(lst)):
            return False
        eq = True
        for number in xrange(0,10):
            if(data_lst[number]!=lst[number]):
                eq=False
        return eq
    def AllRepeatCheck(self,lst):#多字断
        pass
# if __name__ == '__main__':
#     print('[wxpython.py] architecture=%s-bit' % (8 * struct.calcsize("P")))
#     #print('[wxpython.py] wx.version=%s' % wx.version())

#     # Intercept python exceptions. Exit app immediately when exception
#     # happens on any of the threads.
#     sys.excepthook = ExceptHook
#     link=LinkSave()
#     link.load(sys.argv[1])


  