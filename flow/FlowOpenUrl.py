from FlowItem import FlowItem
from FlowManagement import FlowManagement
import time
def consume(manager,url):
	print('Waiting to consume')
	while True:
		manager.LoadUrl(url)
		data = yield
		time.sleep(3)
		print('consumed, the running')
def produce(consumer,context):
	super(FlowOpenUrl,context).Execute()
	consumer.send(None)
	yield
class FlowOpenUrl(FlowItem):
	def __init__(self,url):
		super(FlowOpenUrl,self).__init__(options={'key':'open_url'})
		self.url = url
		self.manager = FlowManagement()
		pass
	def Execute(self,num=-1):
		print(self.manager)
		if (self.manager==None):
			print("FlowOpenUrl  Execute error : not manager")
			return
		if(num==-1):
			self.manager.LoadUrl(self.url)
			print("FlowOpenUrl url:" + self.url)
		else:
			print("FlowOpenUrl url:" + (self.url % num))
			#self.manager.LoadUrl(self.url % num)# %d, not divide!
			consumer = consume(self.manager,self.url % num)
			consumer.send(None)
		#super(FlowOpenUrl,self).Execute()
		producer =  produce(consumer,self)
		next(producer)


