import time
from FlowItem import FlowItem
class FlowWaiting200(FlowItem):
	def __init__(self,url):
		super(FlowWaiting200,self).__init__()
		self.url = url
	def Execute(self):
		# url = getattr(self,'href',self.url)
		# if (url==""):
		url = self.url
		self.manager.url = url
		count = 0
		while(self.manager.CheckIsLoading()==True):
			count +=1
			print('FlowWaiting200 Execute'+str(count))
			time.sleep(1)
		print('FlowWaiting200 finished')
		super(FlowWaiting200,self).Execute()