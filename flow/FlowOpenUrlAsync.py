from FlowItem import FlowItem
import time
class FlowOpenUrlAsync(FlowItem):
	def __init__(self,manager,url):
		super(FlowOpenUrlAsync,self).__init__(manager=manager,options={'key':'open_url_async'})
		self.url = url
	def Execute(self):

		i = 10
		self.manager.LoadUrl(self.url)		
		while(i>=0):
			print('FlowOpenUrlAsync Execute')
			time.sleep(1)
			i-=1

		super(FlowOpenUrlAsync,self).Execute()