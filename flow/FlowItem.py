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
		''' Add by Sidney on 20160127
			If it contains manager, it will naturally deliver it to its decorate target
			It means that this function will cover the target's manager
			And this function is not sure it will lead manager to unclose states for it will be delivered much,
			Obviousely, manager may pass as many times as its decorate times
			Thie function shoud be always keep on considering. Import!!
		'''
		if (self.manager):
			self.component.manager = self.manager
	def Execute(self):
		print("flowitem Execute...")
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