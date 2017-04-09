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

class oldGiftSelector ( giftSelector ):
		"Defining the abstrsct method of parent class"
		def gifting(self, b, g, gift):
				'''Assigning Gifts given by boy to girl'''
				gList = []
				if(b.types == 'miser'):
						b.__class__ = miserBoy
						gList = b.assignGift(g,gift)
				if(b.types == 'generous'):
						b.__class__ = generousBoy
						gList = b.assignGift(g,gift)
				if(b.types == 'geeks'):
						b.__class__ = geekBoy
						gList = b.assignGift(g,gift)
				return gList
				
