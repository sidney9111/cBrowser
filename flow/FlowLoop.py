from FlowItem import FlowItem
from FlowItem import Locker
class FlowLoop(FlowItem):
	def __init__(self,manager=None):
		super(FlowLoop,self).__init__(manager=manager, options={'key':'loop'})
	def Execute(self):
		print("FlowLoop. exe")
		super(FlowLoop,self).Log("flowloop exe")

		self.locker = Locker("flowloop_locker",self.AsyncFunction)
		self.locker.start()
		# if self.options:
		# 	start = self.options['start']
		# 	end = self.options['end']
		# 	obj = self.options['item']
		# 	for i in range(start,end):
		# 		print("flowloop"+str(i))
		# 		obj.Execute()
		# #print(super().options)
		# super(FlowLoop,self).Execute()
	def AsyncFunction(self):
		print("flowloop function")
		if self.options:
			start = self.options['start']
			end = self.options['end']
			obj = self.options['item']
			for i in range(start,end):
				#print("flowloop"+str(i))
				obj.Execute()
	def setOptions(self,opt):
		#hasattr
		if(self.options['key']!=None):
			opt['key']=self.options['key']
		print(self.options)
		print('flowloop setoption')
		print(opt)
		self.options = opt
