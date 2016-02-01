from FlowItem import FlowItem
import time
class FlowJavascriptAsync(FlowItem):
	def __init__(self,js,opt={}):
		super(FlowJavascriptAsync,self).__init__(options={'key':'javascript_async'})
		self.js = js
		self.opt = opt
		if(hasattr(self.options,'lockjs')==False):
			self.options['lockjs']=True
	def Execute(self):
		if(self.options['lockjs']==True):
			self.manager.Lock()
		self.manager.ExecuteJavascript(self.js)
		if(self.options['lockjs']==True):
			while (self.manager.lock==True):
				print("FlowJavascriptAsync waiting...")
				time.sleep(1)

		super(FlowJavascriptAsync,self).Execute()