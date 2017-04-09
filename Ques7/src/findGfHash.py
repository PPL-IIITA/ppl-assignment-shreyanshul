from findGf import findGf
class findGfHash( findGf ):

	def hashing( self, astring, tablesize):
		"Get hash value of given String"
		sum = 0
		for pos in range( len(astring)):
			sum = sum + ord( astring[pos])
		return sum%tablesize
  		
	def makeHashTable( self, couples):
		"Make Hash Table"
		table = {}
		for i in couples:
			table[self.hashing(i[1].name, 101)] = i[0].name
		return table
			
	def find( self, boys, couples ):
		"Find the girlfriend"
		hashTable = {}
		gfList = []
		hashTable = self.makeHashTable( couples)
		for b in boys:
			if self.hashing( b, 101) in hashTable:
				gfList += [ hashTable[self.hashing(b,101) ] ]
			else :
				gfList += ["No Girlfriend"] 
		return gfList
