from FlowItem import FlowItem
from FlowManagement import FlowManagement
import time
import thread
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
mylock = thread.allocate_lock()  #Allocate a lock  
def timer(manager,url,parent):
	mylock.acquire() 
	manager.LoadUrl(url)
	while (manager.CheckIsLoading()==True):
		time.sleep(2)
	parent.Log("loaded %s end:"% url)
	parent.Execute()

	mylock.release()  #Release the lock.  
class FlowOpenUrl(FlowItem):

	def __init__(self,manager=None,url=""):
		super(FlowOpenUrl,self).__init__(manager=manager,options={'key':'open_url'})
		self.url = url
		#self.manager = FlowManagement()
		pass
	def Execute(self,num=-1):
				
		super(FlowOpenUrl,self).Log("Flow open url Execute")
		if (self.manager==None):
			print("FlowOpenUrl  Execute error : not manager")
			return
		url = self.url
		if(num!=-1):
			url = self.url % num
		thread.start_new_thread(timer, (self.manager,url,super(FlowOpenUrl,self))) 
		print("FlowOpenUrl url:" + url)
		# self.manager.LoadUrl(self.url % num)# %d, not divide!
		# consumer = consume(self.manager,self.url % num)
		# consumer.send(None)
		
		# producer =  produce(consumer,self)
		# next(producer)


