import Utils
class FlowItem(object):
	def __init__(self,manager=None,options={}):
		#{'key':'normal'}
		#self.options = options
		if (options=={}):
			self.options = {'key':'item'}
		else:
			self.options = options
		self.component = None
		if(manager!=None):
			self.manager = manager
	# def Options(self,option):
	# 	if(option.key == "open_url"):
	# 		self.manager.browser.OpenUrl(option.url)
	# 	pass
	def Decorate(self,component):
		self.component = component
	def Execute(self):
		print(self.options)
		#print('FlowItem Executt' + self.options['key'])
		if(self.component):
			self.component.Execute()
		#self.isEnd = True

		pass
	# def CheckExecuted(self):
	# 	return self.isEnd
	def Log(self,string):
		if (self.manager):
			self.manager.preference.monitorFrame.Log(str(string))