from random import uniform as bell
from random import choice as select
def formalize(number):
	if number <40:
		number = 40
	elif number >6000:
		number = 6000
	number = float("{0:.3f}".format(number))
	return number

def normalestimation(samplertt,counter):
	x = bell(0.7,1.3)
	y = bell(-10,35)
	estimate = formalize(x*samplertt[-1]+y)
	samplertt.append(estimate)
	counter += 1
	return samplertt,counter

def dostuff(samplertt,counter):
	ring = select([0.25,0.5,0.75,1])
	temp = 0 
	if ring == 0.25:
		temp = formalize(1.85*samplertt[-1])
		samplertt.append(temp)
		counter += 1
	elif ring == 0.5:
		temp = formalize(0.65*samplertt[-1])
		samplertt.append(temp)
		counter += 1
	elif ring == 0.75:
		temp2 = formalize(1.6*samplertt[-1])
		samplertt.append(temp2)
		counter += 1
		if counter+1 <200:
			temp3 = formalize(0.7*samplertt[-1])
			samplertt.append(temp3)
			counter += 1
	else:
		samplertt,counter = normalestimation(samplertt,counter)
	return samplertt,counter

def roundtriptimes():
	samplertt = []
	samplertt.append(100) # this is the initial value
	counter = 0
	while counter<199:
		if counter<19:
			samplertt,counter = normalestimation(samplertt,counter)
		else:
			if counter%5==0:
				samplertt,counter = dostuff(samplertt,counter)
			else:
				samplertt,counter = normalestimation(samplertt,counter)
	return samplertt

def EstimateRTT(samplertt,a):
	Estimatertt = []
	Estimatertt.append(100)
	for i in range(len(samplertt)-1):
		temp = (1-a)*Estimatertt[i] + a*samplertt[i+1]
		temp = float("{0:.3f}".format(temp))
		Estimatertt.append(temp)
	return Estimatertt

def Devrtt(samplertt,estimatertt,b):
	devrtt = []
	devrtt.append(100)
	for i in range(len(samplertt)-1):
		temp = (1-b)*devrtt[i] + b*abs(samplertt[i+1]-estimatertt[i])
		temp = float("{0:.3f}".format(temp))
		devrtt.append(temp)
	return devrtt

def timeoutintervals(estimatertt,devrtt):
	timeoutintervals = []
	for i in range(len(estimatertt)):
		timeoutintervals.append(estimatertt[i]+4*devrtt[i])
	return timeoutintervals
	
def retransmissions(timeoutintervals,samplertt):
	retransmissions = {}
	counter = 0
	for i in range(19,len(samplertt)):
		if timeoutintervals[i-1] > samplertt[i]:
			retransmissions[i] = 1 #succesfull
		elif timeoutintervals[i-1] <= samplertt[i]:
			retransmissions[i] = 0 #unsuccesfull
			counter += 1 #counts the number of retransmissions
	return retransmissions,counter
	
listofsrtts=[] #calculate samplertts'
for i in range(5):
	temp = roundtriptimes()
	listofsrtts.append(temp)

B = [(0.125,0.125),(0.125,0.25),(0.125,0.375)] #the tuples have the form (a,b)
A = [(0.4,0.25),(0.25,0.25)] # same with this one
concat = B+A

retransmissions_dict = {}
retrcounter = {}
dev_dict = {}
estimation_dict = {}
timeout = {}
iterator = 0 
f1 = open('a,b_results_allsrt.txt','w')
for i in listofsrtts:
	for a,b in concat:
		estimation_dict[(a,b,iterator)] = EstimateRTT(i,a)
		dev_dict[(a,b,iterator)] = Devrtt(i,estimation_dict[(a,b,iterator)],b)
		timeout[(a,b,iterator)] = timeoutintervals(estimation_dict[(a,b,iterator)],dev_dict[(a,b,iterator)])
		retransmissions_dict[(a,b,iterator)],retrcounter[(a,b,iterator)] = retransmissions(timeout[(a,b,iterator)],i)
	
	iterator+=1 #indicates the number of the samplertt set

for j in range(iterator):
	f1.write("for the set %d \n"%j)
	for a,b in concat:
		print "for a,b ({0} , {1}) we have {2} retransmissions".format(a,b,retrcounter[(a,b,j)])
		f1.write("for a,b = ({0},{1}) we have {2} retransmissions \n".format(a,b,retrcounter[(a,b,j)]))
f1.close()
f2 = open('set0_quadruples.csv','w')
f2.write('n,timeoutinterval,samplertt,retransmission \n')
for a,b in concat:
	f2.write("\n a,b = ({0},{1}) \n".format(a,b))
	for i in range(100,200):
		print i+1,timeout[(a,b,0)][i-1],listofsrtts[0][i],retransmissions_dict[(a,b,0)][i]
		f2.write("{0} , {1} , {2} , {3} \n".format(i+1,timeout[(a,b,0)][i-1],listofsrtts[0][i],retransmissions_dict[(a,b,0)][i]))
