from FlowItem import FlowItem
import time
class FlowOpenUrlAsync(FlowItem):
	def __init__(self,manager=None,url=""):
		super(FlowOpenUrlAsync,self).__init__(manager=manager,options={'key':'open_url_async'})
		print('FlowOpenUrlAsync manager=',manager)
		self.url = url
	def Execute(self):
		self.manager.LoadUrl(self.url)		
		while(self.manager.CheckIsLoading()==True):
			print('FlowOpenUrlAsync Execute')
			time.sleep(1)

		super(FlowOpenUrlAsync,self).Execute()