from FlowItem import FlowItem
import thread,time
class FlowClick(FlowItem):
	def __init__(self):
		super(FlowClick,self).__init__()
	def Execute(self):
		# thread.start_new_thread(super(FlowClick,self).locker, (self)) 
		print("flowclick Execute")
		# if (self.locker.isAlive())==Flase
		# self.locker.start()
		#js = "$('.next').click()"
		# js = "$('.next>a').bind('click',function(){window.location.href=this.href;});$('.next>a').click();"
		# self.manager.ExecuteJavascript(js)