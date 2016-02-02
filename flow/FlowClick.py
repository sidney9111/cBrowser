from FlowItem import FlowItem
import thread,time
class FlowClick(FlowItem):
	def __init__(self,manager=None,options = {}):
		super(FlowClick,self).__init__(manager=manager,options=options)
	def Execute(self):
		# if (self.locker.isAlive())==Flase
		# self.locker.start()
		#js = "$('.next').click()"
		# this js using window.location to direct url, that could not be trace by python
		# it may not useful in my flow system, so remark this time for further research
		#js = "$('.next>a').bind('click',function(){window.location.href=this.href;});$('.next>a').click();"
		#self.manager.ExecuteJavascript(js)
		self.manager.Lock()
		
		if(self.options['selector']!=None):
			className = self.options['selector']
		else:
			className = ".next>a"
		#js ="exmanager.TestPythonCallback($('%s').attr('href'));" % className
		js ="exmanager.TestPythonCallback($('%s').attr('href'));" % className
		print(js)
		self.manager.ExecuteJavascript(js)
		
		while (self.manager.lock==True):
			print("flowclick Execute waiting")
			time.sleep(1)
		print("FlowClick url="+str(self.manager.lockargs))
		self.Log("-"+str(self.manager.lockargs))
		url = self.manager.GetBrowser().GetMainFrame().GetUrl()
		print(url)
		# #http://
		pos = url[7:].find("/")
		# print(pos)
		pos = pos + 7
		# print(pos)
		# print("&&&&&")
		# print("&&&&&%%%%%")
		# print(url[:pos])
		# print("&&&&&%%%%%%")
		self.Log("--"+url[:pos]+self.manager.lockargs)
		self.manager.LoadUrl(url[:pos]+self.manager.lockargs)
		#self.manager.LoadUrl(self.manager.lockargs)
		count = 0
		while (self.manager.CheckIsLoading()==True):
			count+=1
			print("flowclick load waiting"+str(count))
			time.sleep(1)
		super(FlowClick,self).Execute()