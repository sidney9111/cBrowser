import imp
class ScriptRunner():
	def __init__(self):
		pass
	def Execute(self,browser):
		print("ScriptRunner....................Execute")
		if(self.GetActivity()):
			print("ScriptRunner....................runActivity")
			''' We could also use these codes to import :
				import imp
				stringmodule = imp.loadmodule('string',*imp.findmodule('string'))
			'''
			moduleName = self.script_name
			if(self.script_name==""):
				moduleName = "None"

			fp, pathname, desc = imp.find_module(moduleName, ['./asserts/scripts'])
			meiturnModule = imp.load_module(moduleName, fp, pathname, desc)
			meiturnClass = getattr(meiturnModule, "meituanBehavior")()
			meiturnClass.Run(browser)
	def SetScript(self,name):
		self.script_name = name
	def SetActivity(self,bol):
		self.activity = bol
	def GetActivity(self):
		if (self.activity):
			return True
		else:
			return False
