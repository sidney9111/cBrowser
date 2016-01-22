import Utils
class FlowItem:
	def __init_(self,manager):
		self.manager = manager
	def Options(self,option):
		if(option.key == "open_url"):
			self.manager.browser.OpenUrl(option.url)
		pass
	def Execute(self):
		self.isEnd = true
		pass
	def CheckExecuted(self):
		return self.isEnd
