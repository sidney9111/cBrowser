# -*- coding: UTF-8 -*-
from LinkSave import LinkSave
from scrapy.selector import HtmlXPathSelector
class jianxiong:
	def __int__(self):
		pass
	def SetParent(self,parent):
		self._ = parent

	def Parse(self,string):
		sel = HtmlXPathSelector(text=string)
		main = sel.select('//div[@class="bm vw eis_mtm"]')
		print(str(main))
		item = main.select('./div[@class="fire_float"]')
		href = item.select('./ul/li/div[@class="fire_imgbox"]/a/@href')
		title = item.select('./ul/li/div[@class="fire_imgbox"]/a/@title')
		image = item.select('./ul/li/div[@class="fire_imgbox"]/a/img/@src')

		date = item.select('./ul/li/div[@class="fire_dv"]/span[@class="fire_left"]/text()')
		views = item.select('./ul/li/div[@class="fire_dv"]/span[@class="fire_right"]/text()')
		p = item.select('./ul/li/div[@class="fire_p"]/text()')
		lst = []
		for k,v in enumerate(href):
			lst.append({'href':v.extract()})
		for k,v in enumerate(title):
			lst[k]['title']=v.extract()
		for k,v in enumerate(image):
			lst[k]['image']=v.extract()
		for k,v in enumerate(date):
			lst[k]['date']=v.extract()
		for k,v in enumerate(views):
			lst[k]['views']=v.extract()
		for k,v in enumerate(p):
			lst[k]['p']=v.extract()
		linkSave = LinkSave()
		for k,v in enumerate(lst):
			linkSave.add('data',str(v))