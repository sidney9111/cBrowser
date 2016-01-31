from FlowItem import FlowItem
import time
class FlowJavascriptAsync(FlowItem):
	def __init__(self,js):
		super(FlowJavascriptAsync,self).__init__(options={'key':'javascript_async'})
		self.js = js
	def Execute(self):
		self.manager.ExecuteJavascript(self.js)
		self.manager.Lock()
		while (self.manager.lock==True):
			print("FlowJavascriptAsync waiting...")
			time.sleep(1)

		super(FlowJavascriptAsync,self).Execute()