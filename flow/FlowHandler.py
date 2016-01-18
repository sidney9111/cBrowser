# -*- coding: UTF-8 -*-
'''
2016.01.13 by Sidney 
分享代码啦,基于python2.7
2年lua，多年java经验，新学python，一齐学习吧
上面第一行备注coding: UTF-8，中文备注必须

另外一个py文件可这么import,若此文件放在flow目录下
sys.path.append("flow")
import FlowHandler from FlowHandler

下面首先定义了一个glodal函数flowprint，打印输出用
'''
from LinkSave import LinkSave
from HtmlAnalyzer import HtmlAnalyzer
#import FlowConst
import wx
def flowprint(*msg):
	#支持可变长参数
	#*msg ()
	#**msg [] 貌似python 2.7没用,不确定
	s = ""
	for i,element in enumerate(msg):
		s = s+str(element)
	print('[--flow--print]'+s)
class FlowHandler:			#定义一个普通类，如果是集成类需要带括号，例如：FlowHandler(wx.Frame)
	items={'a':'bbc','i':3}, #定义json格式，可直接获取value=items['i']#变量的作用域为模组级别，可以直接self.item获取
	stateChange =[]
	stateChangeCount=0
	loaded =[]
	loadedCount=0
	loopCount=0
	def __init__(self):
		pass				#不能留空，至少写pass
	def next(self):
		flowprint('s',1,'s')#测试可变参数，字串，对象，数字，bool类型均测试通过
		#print('xx')
	def _loadEnded(self):
		pass
	def _onLoadingStateChange(self,browser, isLoading, canGoBack,canGoForward):
		flowprint(browser,isLoading,canGoBack,canGoForward)
		flowprint('11111111111111111111111111111111111111111111111111111111111')
		self.stateChangeCount+=1
		self.stateChange.append({'url':browser.GetUrl(),'l':isLoading})
		#奇怪的stateChangecount=2，但是stateChange只会apped一次
		#而这一次就是Browser加载完毕的事件，和函数名不符合
		#更奇怪的是第一次执行cefpython ,只执行一次，但按ongo button是执行2次的
	def _onLoaded(self,browser, frame, httpStatusCode):
		#self.items['i']=self.items['i']-1
		#flowprint(self.items['i'])#模组级变量 以及
		if frame == browser.GetMainFrame():
			print "Finished loading main frame: %s (http code = %d)" % (frame.GetUrl(), httpStatusCode)
		flowprint('22222222222222222222222222222222222222222222222222222222222222|'+str(httpStatusCode))
		self.loadedCount+=1
		self.loaded.append(browser.GetUrl())
		print("FlowHandler url="+browser.GetUrl())
		print("FlowHandler on loaded"+str(self.loadedCount)+"|"+str(self.stateChangeCount)) #5|2
	
		# self.browser=browser
		# self.stringVisitor = SouceVisitor(self)
		# browser.GetMainFrame().GetSource(self.stringVisitor)
	def reset(self):
		self.stateChange =[]
		self.stateChangeCount=0
		self.loaded =[]
		self.loadedCount=0
		self.browserLoadedFlag = False

class StringVisitor:
    def Visit(self, string):
    	flowprint("flowhandler Visit")
    	link=LinkSave()
    	link.save("www.baidu.com",string)
    	print("string visitores\n")
    	#reload(FlowConst)
    	#print(FlowConst.getPath())
    	s=link.read("www.baidu.com")
    	ana=HtmlAnalyzer()
    	ana.parse(s)
    	print('self.count',self.stateChangeCount)
class SouceVisitor:
	def __init__(self,parent):
		self.parent=parent
	def Visit(self,string):
		flowprint("flowhandler Visit")
		# link=LinkSave()
		# link.add("www.baidu.com",string)
		
		# s=link.read("www.baidu.com")
		ana=HtmlAnalyzer()
		ana.parse(string)
		self.parent.loopCount+=1
		if(self.parent.loopCount<=10):    		#翻页
			self.parent.browser.GetMainFrame().ExecuteJavascript("$('.page__next').find('span').click();")
class LoadHandler:#同一个py文件，定义的第二个类
	def __init__(self):
		pass
	def dep(self):
		flowprint('testing module function')#global级的方法，这里也可以调用打印