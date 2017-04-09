from girl import girl
from boy import boy
from gifts import gifts
from miserBoy import miserBoy
from generousBoy import generousBoy
from geekBoy import geekBoy
from choosyGirl import choosyGirl
from normalGirl import normalGirl
from desperateGirl import desperateGirl
from abc import ABCMeta, abstractmethod
class giftSelector:

		__metaclass__ = ABCMeta
		"Making Abstract Function of gifting" 
		def gifting(self, b, g, gift ): pass
