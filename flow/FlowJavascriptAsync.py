from FlowItem import FlowItem
import time
class FlowJavascriptAsync(FlowItem):
	def __init__(self,js,options={}):
		super(FlowJavascriptAsync,self).__init__(options=options)
		self.js = js
		if(self.options.has_key('lockjs')==False):
			self.options['lockjs']=True
			
	def Execute(self):
		if(self.options['lockjs']==True):
			self.manager.Lock()
		self.manager.ExecuteJavascript(self.js)
		if(self.options['lockjs']==True):
			while (self.manager.lock==True):
				print(str(self.options))
				print("FlowJavascriptAsync waiting...")
				time.sleep(1)

		super(FlowJavascriptAsync,self).Execute()