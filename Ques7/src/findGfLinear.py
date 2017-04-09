from findGf import findGf
class findGfLinear( findGf ):
	"Linear searching method for serching girlfriends"
	def find( self, boys, couples ):
		"Find the girlfriend"
		gfList = []
		for b in boys:
			flag = 0
			for j in couples:
				if b == j[1].name:
					gfList += [ j[0].name ]
					flag = 1
					break
			if flag == 0:
				gfList += ["No girlfriend"]
		return gfList
