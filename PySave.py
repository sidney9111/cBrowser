# -*- coding:utf-8 -*-
import urllib2
import os
class PySave:
	def __int__(self):
		pass
	def setSite(self,site):
		print('setsite='+site)
		strs=str.split(site,'/')
		self.name = strs[len(strs)-2]
		self.pre=''
		for i in range(0,len(strs)-1):
			self.pre=self.pre+'/'+strs[i]
		self.pre=self.pre[1:]

	def saveUrl(self,url):
		try:
			print('pre='+self.pre)
			print('name='+self.name)
			#判断是否外链
			if len(url)>len(self.pre):
				if url[:len(self.pre)]==self.pre:
					print("pre ="+self.pre+"|"+url)
					local = self.makedirs(url,self.pre)
					print("save file name="+local)
					if url[len(url)-3:]=='png' or url[len(url)-3:]=='jpg':
						try:
							conn = urllib2.urlopen(self.parseUrl(url))
							f = open(local,'wb')
							f.write(conn.read())
							f.close()  
						except Exception,e:#httperror
							self.record('['+str(e)+']'+url,False)
					else:
						try:
							page=self.getPage(url)
							f=open(local,'w')
							f.write(page)
							f.close()
						except Exception,e:#httperror
							self.record('['+str(e)+']'+url,False)
				else:
					self.record(url,False)
			else:
				self.record(url,False)
		except AttributeError:
			print('siteReader reply data error')
	def makedirs(self,site,pre):
		siteList=str.split(site,'/')
		preList=str.split(pre,'/')
		lSite=len(siteList)
		lPre=len(preList)
		url='/'+self.name
		#range 的取值，不包括边界值
		for i in range(lPre,lSite-1):
			#print(i)
			#print("site="+siteList[i])
			url=url+'/'+siteList[i]

			#print('url='+url[1:])
			#if i!=lSite-1:
			if not os.path.exists(url[1:]):
				os.makedirs(url[1:])		
				print('makedirs4444444444',url[1:])
		return url[1:]+'/'+siteList[lSite-1]
	def record(self,url,bol):
		if not os.path.exists(self.name):
			os.makedirs(self.name)
		if bol==True:
			f=open(self.name+'/sits_uncaptured.txt','w')
		else:
			f=open(self.name+'/sits_uncaptured.txt','a')
		f.write(url + '\n')
		f.close()
	def getPage(self,url):
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		#return response.read().decode('utf-8')
		#return response.read().decode('utf-8')
		return response.read()
	def parseUrl(self,url):
		url=url.replace(' ','%20')
		return url