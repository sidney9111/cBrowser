from FlowItem import FlowItem
from scrapy.selector import HtmlXPathSelector
class FlowSimulateClick(FlowItem):
	def __init__(self,manager=None,options={}):
		super(FlowSimulateClick,self).__init__(manager=manager,options=options)
	def Execute(self):
		self.source= SourceVisitor(self)
		self.manager.GetBrowser().GetMainFrame().GetSource(self.source)
		self.super = super(FlowSimulateClick,self)
		super(FlowSimulateClick,self).Execute()
		
class SourceVisitor(object):
	def __init__(self,parent):
		self.parent = parent
	def Visit(self,string):
		sel = HtmlXPathSelector(text=string)
		main = sel.select('//a[@class="nxt"]/@href')

		url = self.parent.manager.GetBrowser().GetMainFrame().GetUrl()
		pos = url[7:].find("/")
		pos = pos + 7

		self.parent.component.href = url[:pos] + str(main[0].extract())
		
