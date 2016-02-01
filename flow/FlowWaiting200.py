import time
from FlowItem import FlowItem
class FlowWaiting200(FlowItem):
	def __init__(self,url):
		super(FlowWaiting200,self).__init__()
		self.url = url
	def Execute(self):
		#self.manager.LoadUrl(self.url)		
		self.manager.url = self.url
		while(self.manager.CheckIsLoading()==True):
			print('FlowWaiting200 Execute')
			time.sleep(1)
		print('FlowWaiting200 finished')
		super(FlowWaiting200,self).Execute()