from FlowItem import FlowItem
import thread,time
from scrapy.selector import HtmlXPathSelector
class FlowRedirect(FlowItem):
	def __init__(self,className):
		super(FlowRedirect,self).__init__()
	def Execute(self):
		jsframe = self.manager.GetBrowser().GetMainFrame()
		self.stringVisitor = SourceVisitor()
		jsframe.GetSource(self.stringVisitor)
		#jsframe.ExecuteJavascript ("$('.page__next').find('span').click();")
		super(FlowScrapy,self).Execute()
class SourceVisitor:
	def __init__(self,parent):
		self.parent = parent
	def Visit(self,string):
		sel = HtmlXPathSelector(text=string)
		next = self.select('//div[@class="paginator-wrapper"]/li[@class="next"]/a/@href')
		next[0].extract()