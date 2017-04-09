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
from giftSelector import giftSelector
from oldGiftselector import oldGiftSelector
from newGiftselector import newGiftSelector
from random import randint
import csv
from random import choice
from string import ascii_uppercase

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

detail = []
def giftingHappCal( couples, gift,detail ):
		'Find happiness & compatibility of Couples'
		gList = []
		for i in couples :
				b = i[1]
				g = i[0]
				
				t = randint(0,2)
				giftSel = giftSelector()
				if t == 0:
						print t
						giftSel.__class__ = oldGiftSelector
						gList = giftSel.gifting( b, g, gift )
				if t == 1:
						print t
						giftSel.__class__ = newGiftSelector
						gList = giftSel.gifting( b, g, gift )
				logger('Gifting:: Boy: ' + b.name + ' gifted Girlfriend: ' + g.name + ' following Gifts: ' + ' '.join([i.name for i in gList]) )			
				
				'''Calculating Happiness Values for Girls'''
				if(g.types == 'choosy'):
						g.__class__ = choosyGirl
						g.calHappiness(gList)
				if(g.types == 'normal'):
						g.__class__ = normalGirl
						g.calHappiness(gList)
				if(g.types == 'desperate'):
						g.__class__ = desperateGirl
						g.calHappiness(gList)
						
				'''Calculating Happiness Values for Boys'''
				if( b.types == 'miser'):
						b.__class__ = miserBoy
						b.calHappiness( g, gList)
				if( b.types == 'generous'):
						b.__class__ = generousBoy
						b.calHappiness( g )
				if( b.types == 'geek'):
						b.__class__ = geekBoy
						b.calHappiness( g )	
						
				'''Finding Happiness and Compatibility of Couples'''
				coupHapp = b.happiness + g.happiness
				coupComp = b.maint_bud - g.maint_bud + abs( b.attract - g.attract ) + abs( b.intelli_lev - g.intelli_lev )
				
				'''Making list of all associated details of Couples'''
				detail += [ (b, g, gList, coupHapp, coupComp) ]
				

giftingHappCal( gfbf, gift, detail)
		
print
print 'All gift details' 
for i in detail:
		print i[0].name+" gifted " + i[1].name + " following gifts:- " 
		for j in i[2]:
			print j.name
		print

		
			
					
				
				

