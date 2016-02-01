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
		#main = sel.select('//div[@class="poi-tile-nodeal"]')
		main = sel.select('//div[@class="bm vw eis_mtm"]')
		item = main.select('./div[@class="fire_float"]')
		href = item.select('./ul/li/div[@class="fire_imgbox"]/a/@href')
		image = item.select('./ul/li/div[@class="fire_imgbox"]/a/img/@src')
		title = item.select('./ul/li/div[@class="fire_imgbox"]/a/img/@title')
		time = item.select('./ul/li/div[@class="fire_dv"]/span[@class="fire_left"]/text()')
		views = item.select('./ul/li/div[@class="fire_dv"]/span[@class="fire_right"]/text()')
		p = item.select('./ul/li/p[@class="fire_dv"]/text()')
		for i,value in enumerate(href):
			lst.append({'href':href.extract()})

		for i,value in enumerate(image):
			lst[i]['image']=value.extract()
		for i,value in enumerate(title):
			lst[i]['title']=value.extract()
		for i,value in enumerate(time):
			lst[i]['time']=value.extract()
		for i,value in enumerate(views):
			lst[i]['views']=value.extract()
		for i,value in enumerate(p):
			lst[i]['p']=value.extract()
		linkSave = LinkSave()
		for i,value in enumerate(lst):
			linkSave.add("data",str(value))