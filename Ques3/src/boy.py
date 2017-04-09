class boy:

	def __init__ (self, name, attract, maint_bud, intelli_lev, attract_req, types):
		"Initializing variables through constructor"
		self.name = name
		"""@ivar: Boy's Name"""
		self.attract = attract
		"""@ivar: Boy's Attractiveness"""
		self.maint_bud = maint_bud
		"""@ivar: Boy's Maintenance Budget"""
		self.intelli_lev = intelli_lev
		"""@ivar: Boy's Intelligence Level"""
		self.attract_req = attract_req
		"""@ivar: Boy's Attractiveness Requirement"""
		self.rel_stat = 'single'
		self.types = types
		"""@ivar: Boy's Type"""
		self.happiness = 0.0
		"""@ivar: Boy's Happiness"""
