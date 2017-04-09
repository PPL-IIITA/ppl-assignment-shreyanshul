import logging
from girl import girl
from boy import boy
from gifts import gifts
from miserBoy import miserBoy
from generousBoy import generousBoy
from geekBoy import geekBoy
from choosyGirl import choosyGirl
from normalGirl import normalGirl
from desperateGirl import desperateGirl
from random import randint
import csv
from random import choice
from string import ascii_uppercase
from findGf import findGf
from findGfBinarySearch import findGfBinarySearch
from findGfHash import findGfHash
from findGfLinear import findGfLinear

def writeInCSV(Data,filename):
	' To write the CSV files '
	w = csv.writer(open(filename,'wb'), delimiter=',') 
	for line in Data:
		w.writerow(line)
		
def generate():
	' To make test cases '
	boyType = [ 'miser', 'generous' , 'geek' ]
	girlType = [ 'choosy' , 'desperate' , 'normal' ] 
	giftType = [ 'luxury' , 'essential' , 'utility' ]
	
	writeInCSV( [('boy '+ str(i) + ''.join(choice(ascii_uppercase) for i in range(3)),randint(0,10),randint(0,200),randint(0,10),randint(0,10),boyType[randint(0,2)]) 
				for i in range(0,30)],'boy.csv')
	writeInCSV([('girl '+ str(i) +''.join(choice(ascii_uppercase) for i in range(3)),randint(0,10),randint(0,200),randint(0,10),girlType[randint(0,2)])
				for i in range(0,15)],'girl.csv')
	writeInCSV([('gift '+ str(i) +''.join(choice(ascii_uppercase) for i in range(5)),randint(0,10),randint(0,10),giftType[randint(0,2)] )
				for i in range(0,10)],'gift.csv')
	
			
def logger(information) :
	' Generates Log file ' 
	logging.basicConfig(filename='logFile.log', level=logging.DEBUG, format='%(asctime)s  - %(message)s - %(levelname)s')
	logging.info(information)
def eligible(b,g):
	' Check the eligibility of boy & girl for coupling '
	temp = True
	if( (b.rel_stat == 'commited') or (g.rel_stat == 'commited')) :
		 temp = False
	if( b.maint_bud < g.maint_bud ):
		temp = False
	if( b.attract_req > g.attract ):
		temp = False
	return temp
	
	
generate() 
readBoy = csv.reader(open('boy.csv'), delimiter = ',')
readGirl = csv.reader(open('girl.csv') , delimiter = ',')
readGift = csv.reader( open('gift.csv'),delimiter = ',' )

g1 = [ girl(row[0],int(row[1]),int(row[2]),int(row[3]),row[4]) for row in readGirl]
b1 = [ boy(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), row[5]) for row in readBoy] 
gift = [ gifts(row[0], int(row[1]), int(row[2]), row[3]) for row in readGift]

gfbf = []  #list of couples
"List of Couples"
def makeCouple(gfbf):
	'Make couples'
	for g in g1 : 
		for b in b1 : 
		
			if( eligible(b,g) ):
			
				logger(g.name + " is commited with " + b.name)
				g.rel_stat = 'commited'
				b.rel_stat = 'commited'
				gfbf += [(g,b)]
				break
makeCouple(gfbf)

"Select random boys to check for their girlfriends"
length = len(b1)
ran = randint(1,length-1)


def getBoysList():
	"Generate list of boys"
	boyList = []
	for i in range ( 0, ran):
		j = randint( 0, length-1)
		boyList += [b1[j].name];
	for i in range(0 ,ran):
		print boyList[i]
	return boyList


def findGirlFriend( boyList, couples ):
	"Find the girlfriends(if exists)"
	findGirls = findGf()
	gfList = []
	rando = randint(0,2)
	if rando == 0 :
		findGirls.__class__ = findGfBinarySearch
		gfList = findGirls.find( boyList, couples)
	if rando == 1:
		findGirls.__class__ = findGfHash
		gfList = findGirls.find( boyList, couples)
	else:
			findGirls.__class__ = findGfLinear
			gfList = findGirls.find( boyList, couples)
	for i in range( 0, ran ):
		print boyList[i] + " is coupled with " + gfList[i]

findGirlFriend( getBoysList(), gfbf )
		
			
					
				
				

