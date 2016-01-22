# -*- coding: UTF-8 -*-
from LinkSave import LinkSave
from scrapy.selector import HtmlXPathSelector
class meituanfood:
	def __int__(self):
		pass
	def Run(self,browser):
		jsframe = browser.GetMainFrame()
		self.browser = browser
		self.stringVisitor = SourceVisitor(self)
		jsframe.GetSource(self.stringVisitor)
		index = browser.GetUrl().find('/',7)#前面6个字符：http://，从7开始
		self.urlFront = browser.GetUrl()[:index]
		print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
		print(self.urlFront)
		#jsframe.ExecuteJavascript ("$('.page__next').find('span').click();")
class SourceVisitor:# 这个类无需写接口，但可直接实现接口
	def __init__(self,parent):
		self.parent=parent # self.parent已弃用，只是示范，可以直接这样实现Visitor接口
	def Visit(self,string):# 这里其实直接实现Visitor接口的Visit方法(应该是根据方法名实现）
		sel = HtmlXPathSelector(text=string)
		url = sel.select('//li[@class="next"]/a/@href').extract()[0]
		print('meituanfood:'+url)
		self.parent.browser.LoadUrl(self.parent.urlFront+url)
		pass