from gifts import gifts
class utilGifts( gifts ):
	
	def __init__( self, name, price, value, types, utilVal, utilClass ):
		"Constructor for intializing"
		self.utilVal = utilVal
		"""@ivar: Utility Value of Gift"""
		self.utilClass = utilClass
		"""@ivar: Utility Class of Gift"""
		gifts.__init__(name, price, value, types) 
		

