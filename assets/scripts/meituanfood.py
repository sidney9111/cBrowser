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
	def SetParent(self,parent):
		self._ = parent

	def Parse(self,string):
		sel = HtmlXPathSelector(text=string)
		#main = sel.select('//div[@class="poi-tile-nodeal"]')
		main = sel.select('//div[contains(@class,"poi-tile-nodeal")]')
		div = main.select('./div[@class="poi-tile__info"]')
		title_cf = div.select('./div[@class="basic cf"]/a/text()')
		self._.Log(len(title_cf))
		lst = []
		for i,value in enumerate(title_cf):
			lst.append({'name':value.extract().decode()})
		rate = div.select('./div[@class="extra"]/div[@class="rate"]/a/span/text()')
		for i,value in enumerate(rate):
			lst[i]['rate']=value.extract()
		category = div.select('./div[@class="extra"]/div[@class="tag-list"]')
		for i,value in enumerate(category):
			lst[i]['c1']=value.select('./a/text()')[0].extract().encode('utf-8')
			lst[i]['c2']=value.select('./a/text()')[1].extract()
		price2 = main.select('./div[@class="poi-tile__money"]/span[@class="avg"]/span/text()')
		for i,value in enumerate(price2):
			lst[i]['p2']=value.extract()
		price1 = main.select('./div[@class="poi-tile__money"]/a[@class="price f2"]/span/text()')
		for i,value in enumerate(price1):
			lst[i]['p1']=value.extract()
		href = main.select('./a[@class="poi-tile__head"]/@href')
		print(len(lst))
		for i,value in enumerate(href):
			print(i)
			lst[i]['href'] = value.extract()
		img = main.select('./a[@class="poi-tile__head"]/img/@src')
		for i,value in enumerate(img):
			lst[i]['img']=value.extract()
		for i,value in enumerate(lst):
			self._.Log(value)
class SourceVisitor:# 这个类无需写接口，但可直接实现接口
	def __init__(self,parent):
		self.parent=parent # self.parent已弃用，只是示范，可以直接这样实现Visitor接口
	def Visit(self,string):# 这里其实直接实现Visitor接口的Visit方法(应该是根据方法名实现）
		sel = HtmlXPathSelector(text=string)
		url = sel.select('//li[@class="next"]/a/@href').extract()[0]
		print('meituanfood:'+url)
		self.parent.browser.LoadUrl(self.parent.urlFront+url)
		pass