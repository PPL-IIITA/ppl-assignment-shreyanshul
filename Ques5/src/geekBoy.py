from boy import boy
class geekBoy( boy ):

	def __init__ (self, name, attract, maint_bud, intelli_lev, attract_req,types):
			"Constructor for intializing"
			boy.__init(  name, attract, maint_bud, intelli_lev, attract_req,types)
			

	def calHappiness( self, partner ):
			"Calculate Happiness for Geek Boy"
			self.happiness = partner.intelli_lev
			

	def assignGift(self, girl, gifts):
			"Gifts gifted by Geek Boy"
			gifts = sorted( gifts, key = lambda x : x.price)
			maxim = 0
			giftBasket = []
			for i in gifts:
					if( maxim  < girl.maint_bud ):
							maxim += i.price
							giftBasket += [ i ]
					else:
						break
			if (maxim > self.maint_bud) :
					self.maint_bud = maxim
			else:
				if (self.maint_bud > maxim) :
						for i in gifts:
								if (i.types == 'luxury' and ((i not in giftBasket) and (i.price <= (self.maint_bud-maxim) ) ) ):
										giftBasket += [ i ]
			return giftBasket
			 
					
							
							
					
