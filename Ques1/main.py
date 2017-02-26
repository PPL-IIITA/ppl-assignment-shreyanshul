import logging
from q1girl import girl
from q1boy import boy
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
	writeInCSV( [('boy '+ str(i) + ''.join(choice(ascii_uppercase) for i in range(3)),randint(1,10),randint(100,500),randint(1,10),randint(1,10))
				for i in range(0,100)],'boy.csv')
	writeInCSV([('girl '+ str(i) +''.join(choice(ascii_uppercase) for i in range(3)),randint(1,10),randint(100,500),randint(1,10))
				for i in range(0,15)],'girl.csv')
	
			
def logger() :
	' Generates Log file ' 
	logging.basicConfig(filename='q1logFile.log', level=logging.DEBUG, format='%(asctime)s  - %(message)s - %(levelname)s')
	
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
g1 = [ girl(row[0],int(row[1]),int(row[2]),int(row[3])) for row in readGirl]
b1 = [ boy(row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4])) for row in readBoy] 
gfbf = []
for g in g1 : 
	for b in b1 : 
		
		if( eligible(b,g) ):
			
			logger()
			logging.info(g.name + " is commited with " + b.name)
			g.rel_stat = 'commited'
			b.rel_stat = 'commited'
			gfbf += [(g.name,b.name)]
			break
print "\n".join([i[0]+ ' is comitted with ' + i[1] for i in gfbf])
