class girl:

	def __init__ ( self, name, attract, maint_bud, intelli_lev,types) :
		"Initializing variables through constructor"
		self.name = name
		"""@ivar: Name of Girl"""
		self.attract = attract
		"""@ivar: Attractiveness of Girl"""
		self.maint_bud = maint_bud
		"""@ivar: Maintenence Budget of Girl"""
		self.intelli_lev = intelli_lev
		"""@ivar: Intelligence Level of Girl"""
		self.rel_stat = 'single'
		self.types = types
		"""@ivar: Type of Girl"""
		self.happiness = 0.0
		"""@ivar: Happiness of a Girl"""
