from pymongo import MongoClient
from LinkSave import LinkSave
class MongoSave(object):
	"""docstring for MongoSave"""
	def __init__(self, arg):
		super(MongoSave, self).__init__()
		self.arg = arg
		self.client = MongoClient()
	def add(self,str):
		db = self.client.test
		ret = db.meituan.insert_one(str)
		print(ret)
	def read(self):
		
		db = self.client.test
		#coll = db['restaurants']
		cursor = db.restaurants.find({"address.zipcode": "10075"})
		print('xxx')
		for document in cursor:
			print(document)
	def loadDataFile(self):
		link = LinkSave()
		lst = link.readlines("data")
		for item in lst:
			j = eval(item)
			self.add(j)
