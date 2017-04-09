from girl import girl

class normalGirl( girl ):
		
		def __init__(  self, name, attract, maint_bud, intelli_lev,types):
				"Constructor for intializing"
				girl.__init__(  name, attract, maint_bud, intelli_lev,types )
				
		
		def calHappiness( self, giftList  ):
				"Calculate happiness for Normal Girl"
				a = 0
				for i in giftList:
						a = a+ i.value + i.price
				self.happiness = a
