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
def flowprint(*msg):
	#支持可变长参数
	#*msg ()
	#**msg [] 貌似python 2.7没用,不确定
	s = ""
	for i,element in enumerate(msg):
		s = s+str(element)
	print('[--flow--print]'+s)
class FlowHandler:			#定义一个普通类，如果是集成类需要带括号，例如：FlowHandler(wx.Frame)
	items={'a':'bbc','i':3} #定义json格式，可直接获取value=items['i']
							#变量的作用域为模组级别，可以直接self.item获取
	def __init__(self):
		pass				#不能留空，至少写pass
	def next(self):
		flowprint('s',1,'s')#测试可变参数，字串，对象，数字，bool类型均测试通过
		#print('xx')
	def _loadEnded(self):
		pass
	def _loadStatusChange(self):
		pass
	def _onLoadingStateChange(self,browser, isLoading, canGoBack,canGoForward):
		flowprint(browser,isLoading,canGoBack,canGoForward)
	def _onLoaded(self,browser, frame, httpStatusCode):
		#self.items['i']=self.items['i']-1
		#flowprint(self.items['i'])#模组级变量 以及
		#self.stringVisitor = StringVisitor()
		self.stringVisitor = StringVisitor()
		browser.GetMainFrame().GetSource(self.stringVisitor)
		
class StringVisitor:
    def Visit(self, string):
    	flowprint(string)
    	link=LinkSave()
    	link.save("www.baidu.com",string)
class LoadHandler:#同一个py文件，定义的第二个类
	def __init__(self):
		pass
	def dep(self):
		flowprint('testing module function')#global级的方法，这里也可以调用打印