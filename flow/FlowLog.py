from FlowItem import FlowItem
class FlowLog(FlowItem):
	def __init__(self):
		super(FlowLoop,self).__init__()
	def Execute(self):
		print('flowlog .........log')