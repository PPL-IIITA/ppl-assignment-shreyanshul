from girl import girl
from math import exp
class desperateGirl( girl ):
		def __init__(  self, name, attract, maint_bud, intelli_lev,types):
				"Constructor for intializing"
				girl.__init__(  name, attract, maint_bud, intelli_lev,types )
				
		def calHappiness( self, giftList  ):
				"Calculate happiness for Desperate Girl"
				a = 0
				for i in giftList:
						a = a+ i.value + i.price
				a = exp(float(a))
				self.happiness = a
