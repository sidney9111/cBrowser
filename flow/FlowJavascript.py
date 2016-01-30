from FlowItem import FlowItem
import thread,time
class FlowJavascript(FlowItem):
	def __init__(self,js):
		super(FlowJavascript,self).__init__()
		self.js = js
	def Execute(self):
		self.manager.Lock()

		thread.start_new_thread(runner, (self.manager,super(FlowJavascript,self))) 
def runner(manager,parent):
		js = "script=document.createElement('script');script.type='text/javascript';script.src='http://192.168.1.215:8088/animate.js';document.body.appendChild(script);"
		manager.ExecuteJavascript(js)
		while (manager.lock==True):
			print("runner...")
			time.sleep(2)

		parent.Execute()# flow item execute
