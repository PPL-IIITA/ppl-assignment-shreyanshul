from girl import girl
from math import log
class choosyGirl( girl ):
		def __init__(  self, name, attract, maint_bud, intelli_lev,types):
				"Constructor for intializing"
				girl.__init__(  name, attract, maint_bud, intelli_lev,types )
				
		def calHappiness( self, giftList  ):
				"Calculate Happiness for Choosy Girl"
				a = 1
				for i in giftList:
						if( i.types == 'luxury' ):
								a = a + 2*i.value + i.price
						else :
								a = a+ i.value + i.price
				a = log ( a )
				self.happiness = a
