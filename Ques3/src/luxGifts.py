from gifts import gifts
class luxGifts( gifts ):

	def __init__(self, name, price, value, types, rating, difficulty):
		"Constructor for intializing"
       	self.rating = rating
       	"""@ivar: Rating of Gift"""
      	self.difficulty = difficulty
      	"""@ivar: Difficulty to obtain gift"""
      	gifts.__init__( name , price, value, types)
