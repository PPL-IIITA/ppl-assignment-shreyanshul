from giftSelector import giftSelector
from girl import girl
from boy import boy
from gifts import gifts
from miserBoy import miserBoy
from generousBoy import generousBoy
from geekBoy import geekBoy
from choosyGirl import choosyGirl
from normalGirl import normalGirl
from desperateGirl import desperateGirl

class newGiftSelector ( giftSelector ):
		"Defining the abstrsct method of parent class"
		def gifting(self, b, g, gift):
				gList = []
				'''Assigning atleast one Gift of every type is given by boy to girl'''
				if(b.types == 'miser'):
						b.__class__ = miserBoy
						gList = b.assignFirstGift(g,gift)
				if(b.types == 'generous'):
						b.__class__ = generousBoy
						gList = b.assignFirstGift(g,gift)
				if(b.types == 'geeks'):
						b.__class__ = geekBoy
						gList = b.assignFirstGift(g,gift)
						
				if(b.types == 'miser'):
						b.__class__ = miserBoy
						gList += b.assignGift(g,gift)
				if(b.types == 'generous'):
						b.__class__ = generousBoy
						gList += b.assignGift(g,gift)
				if(b.types == 'geeks'):
						b.__class__ = geekBoy
						gList += b.assignGift(g,gift)
				return gList
