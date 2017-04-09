from boy import boy
class miserBoy( boy ):
	def __init__ (self, name, attract, maint_bud, intelli_lev, attract_req,types):
			"Constructor for intializing"
			boy.__init__(  name, attract, maint_bud, intelli_lev, attract_req,types)
			
	def calHappiness( self, partner, giftList ):
			"Calculate Happiness for Miser Boy"
			a = self.maint_bud
			for gift in giftList:
				a = a - gift.price
			self.happiness	 = a
			
	def assignGift(self, girl, gift):
			"Gifts gifted by Miser Boy"
			gift = sorted( gift, key = lambda x : x.price)
			maxim = 0
			giftBasket = []
			for i in gift:
					if( maxim  < girl.maint_bud ):
							maxim += i.price
							giftBasket += [i]
					else:
						break
			if (maxim > self.maint_bud):
					self.maint_bud = maxim
			return giftBasket
	
	def assignFirstGift(self, girl, gift):
			"First Gift gifted by Miser Boy"
			giftBasket = []
			gift = sorted( gift, key = lambda x : x.price)
			giftBasket += [gift[0]]
			if self.maint_bud >= gift[0].price:
					self.maint_bud = self.maint_bud - gift[0].price
			if self.maint_bud < gift[0].price:
					self.maint_bud = gift[0].price + 200
			return giftBasket
							
			
