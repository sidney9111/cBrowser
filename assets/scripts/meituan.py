# -*- coding: UTF-8 -*-
from LinkSave import LinkSave
from scrapy.selector import HtmlXPathSelector
class meituanBehavior:
	def __int__(self):
		pass
	def Run(self,browser):
		print('meituan run')
		jsframe = browser.GetMainFrame()
		self.stringVisitor = SourceVisitor(self)
		jsframe.GetSource(self.stringVisitor)
		
		jsframe.ExecuteJavascript ("$('.page__next').find('span').click();")
class SourceVisitor:# 这个类无需写接口，但可直接实现接口
	def __init__(self,parent):
		self.parent=parent # self.parent已弃用，只是示范，可以直接这样实现Visitor接口
	def Visit(self,string):# 这里其实直接实现Visitor接口的Visit方法(应该是根据方法名实现）
		print("ScriptRunner sourceVisitor Visit")
		# link=LinkSave()
		# link.add("www.baidu.com",string)
		
		# s=link.read("www.baidu.com")
		#ana=HtmlAnalyzer()
		#ana.parse(string)
		sel = HtmlXPathSelector(text=string)
		objects=sel.select('//div[@class="mod-picList"]/div/h3/a')
		lst = []
		
		v=objects.select('./text()')
		for i,value in enumerate(v):
			lst.append([value.extract()])
			#print(value.extract())
		h=objects.select('./@href')
		for i,href in enumerate(h):
			lst[i].append(href.extract())
			#print(href.extract())
		linkSave = LinkSave()
		for key,value in enumerate(lst):
			string = ""
			print(value)
			for i,text in enumerate(value):
				string = string + text + "|"
			linkSave.add("data",string)