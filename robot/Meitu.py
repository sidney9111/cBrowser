# -*- coding: UTF-8 -*-
import urllib
import urllib2
import cookielib
import logging
import logging.config
import time
from scrapy.selector import HtmlXPathSelector
class Meitu:
	def __init__(self,parent=None):
		self.parent=parent
		self.loginURL="http://login.meitu.com/"
		self.post = post = {'username':'15915969279',
			'password':'123456789',
			'remember_me': '0'}
		#登录POST数据时发送的头部信息
		self.loginHeaders =  {
			'Host':'login.taobao.com',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
			'Referer' : 'https://login.taobao.com/member/login.jhtml',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Connection' : 'Keep-Alive'
		}
		self.postData = urllib.urlencode(self.post)
		#设置代理
		#self.proxy = urllib2.ProxyHandler({'http':self.proxyURL})
		#设置cookie
		#self.cookie = cookielib.LWPCookieJar()
		#设置cookie处理器
		#self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
		#设置登录时用到的opener，它的open方法相当于urllib2.urlopen
		#self.opener = urllib2.build_opener(self.cookieHandler,self.proxy,urllib2.HTTPHandler)
		logging.config.fileConfig("./logging.conf")    # 采用配置文件  
		# create logger  
		#self.logger = logging.getLogger("meitu")  
		self.loggerRoot = logging.getLogger("simple")
	def addCart(self):
		post = post = {'speci_id':'207','count':'2'}
		self.postData = urllib.urlencode(post)
		status = self.sendPost()
		print("addcart:" + str(status) + "|count=2")
	def sendPost(self):
		#第一次登录获取验证码尝试，构建request
		request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
		#得到第一次登录尝试的相应
		response = urllib2.urlopen(request)
		status = response.getcode()
		return status
	def main(self):
		#第一次登录获取验证码尝试，构建request
		request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
		#得到第一次登录尝试的相应
		response = urllib2.urlopen(request)
		status = response.getcode()
		print("status="+str(status))
		if status==200:
			self.addCart()
			self.addCart()
	def loop(self,url):
		if url:
			loop = True
			while loop:
				request = urllib2.Request(url)
				response = urllib2.urlopen(request)
				#self.log(response)
				latestTime=self.getLastTime(response)
				print(latestTime)
				if latestTime==True and hasattr(self,"parent"):
					loop=False
					self.parent.ended()
				else:
					self.loggerRoot.debug("loop request=" + url)
					time.sleep(1)

	def getLastTime(self,response):
		sel = HtmlXPathSelector(text=response.read())
		inputObjects=sel.select('//div[@class="p-info"]')
		for index, link in enumerate(inputObjects):
			print(link.extract())
		# inputObjects=sel.select('//span[@class="over-time"]')
		# for index, link in enumerate(inputObjects):
		# 	print(link.extract())
		l=ISOString2Time("2015-05-01 09:00:00")
		now=time.strptime(time.ctime(),"%a %b %d %H:%M:%S %Y")
		print(time.mktime(now))
		print(time.mktime(l))

		if time.mktime(now)-time.mktime(l)>=0:
			return True
		else: 
			return False
	def log(self,response):
		self.logger.debug(response.getcode())
		
		#testType=response.info().getheader("Content-Type")
		testType=response.info()
		if testType:
			self.logger.debug(testType)
		self.logger.debug(response.read()+"*****")
ISOTIMEFORMAT="%Y-%m-%d %X"
def ISOString2Time(s):
	'''
	convert a ISO format time to second
	from:2006-04-12 16:46:40 to:23123123
	把一个时间转化为秒
	'''
	return time.strptime( s,ISOTIMEFORMAT )
# meitu=Meitu()
# l=ISOString2Time("2015-04-30 22:23:00")
# now=time.strptime(time.ctime(),"%a %b %d %H:%M:%S %Y")
# meitu.loggerRoot.debug("bbc")
# print(time.mktime(now)-time.mktime(l))
# meitu.loop()

