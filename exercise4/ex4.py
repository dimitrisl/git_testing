from random import uniform as bell
from random import choice as select
from math import exp

def congevo(congwin,state):
	if state:
		congwin = congwin + 5 #no loss
	else:
		congwin = congwin/2 #loss
	return congwin

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
	congwin = 10
	congwindow = []
	while counter<199:
		if counter>=10:
			coin = bell(0,1)
			probability = 0.6*(1-exp(-congwin/25.0))
			if (coin - probability)<=0:
				congwin = congevo(congwin,False) #here we have segment loss
				congwindow.append(False)
			else:
				congwin = congevo(congwin,True)
				congwindow.append(True)

		if counter<19:
			samplertt,counter = normalestimation(samplertt,counter)
		else:
			if counter%5==0:
				samplertt,counter = dostuff(samplertt,counter)
			else:
				samplertt,counter = normalestimation(samplertt,counter)
	return samplertt,congwindow

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
	
def retransmissions(timeoutintervals,samplertt,congwindow):
	retransmissions = {}
	counter = 0
	for i in range(19,len(samplertt)):
		if (timeoutintervals[i-1] > samplertt[i]) and congwindow[i]:
			retransmissions[i] = 1 #succesfull
		elif timeoutintervals[i-1] <= samplertt[i]:
			retransmissions[i] = 0 #unsuccesfull
			counter += 1 #counts the number of retransmissions
	return retransmissions,counter
	
srtt,congwindows=roundtriptimes()

concat = [(0.125,0.25)]
for a,b in concat:
	estrtt = EstimateRTT(srtt,a)
	devrtt = Devrtt(srtt,estrttm,b)
	timeout = timeoutintervals(estrtt,devrtt)