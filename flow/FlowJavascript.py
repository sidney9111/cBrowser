from FlowItem import FlowItem
class FlowJavascript(FlowItem):
	def __init__(self,js):
		super(FlowJavascript,self).__init__()
		self.js = js
	def Execute(self):
		self.manager.ExecuteJavascript("PyPrint('fff');")
