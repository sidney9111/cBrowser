from FlowItem import FlowItem
class FlowLoop(FlowItem):
	def __init__(self):
		super(FlowLoop,self).__init__(options={'key':'loop'})
	def Execute(self):
		print("FlowLoop. exe")
		if self.options:
			start = self.options['start']
			end = self.options['end']
			obj = self.options['item']
			for i in range(start,end):
				obj.Execute(num=i)
		#print(super().options)
		super(FlowLoop,self).Execute()
	def setOptions(self,opt):
		#hasattr
		if(self.options['key']!=None):
			opt['key']=self.options['key']
		print(self.options)
		print('flowloop setoption')
		print(opt)
		self.options = opt
