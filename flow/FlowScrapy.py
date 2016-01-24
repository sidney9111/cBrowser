from FlowItem import FlowItem
from FlowManagement import FlowManagement
from scrapy.selector import HtmlXPathSelector
import imp
class FlowScrapy(FlowItem):
	def __init__(self,options):
		super(FlowScrapy, self).__init__(options = options)
		self.manager = FlowManagement()
	def Execute(self):
		jsframe = self.manager.GetBrowser().GetMainFrame()
		self.stringVisitor = SourceVisitor(self,self.options)
		jsframe.GetSource(self.stringVisitor)
		#jsframe.ExecuteJavascript ("$('.page__next').find('span').click();")
		super(FlowScrapy,self).Execute()
class SourceVisitor:
	def __init__(self,parent,options):
		self.parent = parent
		self.options = options
	def Visit(self,string):
		if (self.options.has_key('script')):
			#script should not has houzui, because className may refer to script name
			#wrong: meituanfood.py
			#right: meituanfood
			moduleName = self.options['script']
			# if(slef.options['script']==""):
			# 	moduleName = "None"
			className = moduleName
			fp, pathname, desc = imp.find_module(moduleName, ['./assets/scripts'])
			meiturnModule = imp.load_module(moduleName, fp, pathname, desc)
			print("FlowScrapy Visit")
			print(moduleName)
			print(className)
			scriptClass = getattr(meiturnModule, className)()
			scriptClass.SetParent(super(FlowScrapy,self.parent))
			ret = scriptClass.Parse(string)
			return
		sel = HtmlXPathSelector(text=string)
		#url = sel.select('//li[@class="next"]/a/@href').extract()[0]
		#self.parent.browser.LoadUrl(self.parent.urlFront+url)
		self.parent.data = []
		#for k,v in enumerate(self.options):
		# not loop needed, because self.options is columns params
		# it usually loop row as below
		v = self.options
		super(FlowScrapy,self.parent).Log("v:"+str(v))
		index = 0
		if (v.has_key('index')):
			index = v['index']
		rowMax = 1
		if (v.has_key('row')):
			rowMax = v['row']
		for i in range(0,rowMax):
			item = sel.select(v['path'])[i*rowMax + index]
			if (v.has_key('text')):
				item = item.select('./text()')
			super(FlowScrapy,self.parent).Log(item[0].extract())
			
			# if (self.parent.data[k]):
			# 	self.parent.data +=
			# else
			# 	self.parent


