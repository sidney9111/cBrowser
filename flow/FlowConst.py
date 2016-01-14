class FlowConst(object):
 	"""docstring for ClassName"""
 	def __init__(self):
 		super(FlowConst, self).__init__()
 		#self.arg = arg
	# def getPath(self):
	# 	return '1122222222'
def getPath():
	return '444444444444444'
def Read(sel):
	objects=sel.select('//div[@class="mod-picList"]/div/h3/a')
	h=objects.select('./@href')
	for i,href in enumerate(h):
		print(href.extract())
	v=objects.select('./text()')
	for i,value in enumerate(v):
		print(v.extract())
