from boy import boy
class generousBoy( boy ):
	
	def __init__ (self, name, attract, maint_bud, intelli_lev, attract_req,types):
			"Constructor for intializing"
			boy.__init__(  name, attract, maint_bud, intelli_lev, attract_req,types)
			

	def calHappiness( self, partner ):
			"Calculate happiness for Generous Boys"
			self.happiness = partner.happiness
			
	
	def assignGift( self, girl, gifts ):
			"Gifts gifted by Generous Boy"
			maxim = 0
			giftBasket = []
			flag = 0
			gifts = sorted( gifts , key = lambda x : x.price, reverse = True) 
			for i in gifts:
					if( maxim + i.price <= self.maint_bud) :
							maxim += i.price
							giftBasket += [ i ]
							flag = 1
					else :
						break
			if (maxim > self.maint_bud):
					self.maint_bud = maxim
			if( flag == 0 ):
					self.maint_bud = gifts[0].price
					giftBasket += [ gifts[0] ]
			return giftBasket 
