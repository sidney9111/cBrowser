from FlowItem import FlowItem
import time
class FlowOpenUrlAsync(FlowItem):
	def __init__(self,manager=None,url=""):
		super(FlowOpenUrlAsync,self).__init__(manager=manager,options={'key':'open_url_async'})
		print('FlowOpenUrlAsync manager=',manager)
		self.url = url
	def Execute(self):
		url = getattr(self,'href',self.url)
		if (url==""):
			self.manager.LoadUrl("http://www.playno1.com/portal.php?mod=list&catid=78&page=6")		
		else:
			self.manager.LoadUrl(url)		
		while(self.manager.CheckIsLoading()==True):
			print('FlowOpenUrlAsync Execute',url)
			time.sleep(1)

		super(FlowOpenUrlAsync,self).Execute()