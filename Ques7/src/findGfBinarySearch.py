from findGf import findGf
class findGfBinarySearch( findGf ):
	
	def binarySearch(self, alist, item):
		"Binary Search implementation for searching girlfriend"
	  	first = 0
	    	last = len(alist) - 1
	    	found= False
	    	defau = 'No girlfriend'
	    	while first<=last and not found:
        			midpoint = (first + last)//2
	    	 		if alist[midpoint][1].name == item:
	    				found = True
	    	 		elif item < alist[midpoint][1].name:
	    	    	  		last = midpoint-1
	    	       		else:
	  					first = midpoint+1
	  			   	
	    	if (found == True):
					defau = alist[midpoint][0].name	
			
		return defau
		
	def find( self, boys, couples ):
		"Find the girlfriend"
		gfList = []
		couples = sorted( couples, key = lambda x : x[1] )
		for b in boys:
			gf = "null"
			gf = self.binarySearch( couples, b)
			if gf == "null":
				gfList += ["No Girlfriend"]
			else:
				gfList += [ gf ] 
		return gfList
		
	
