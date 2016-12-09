from random import uniform as bell

def normalestimation(samplertt,counter):
	x = float("{0:.3f}".format(bell(0.7,1.3)))
	y = float("{0:.3f}".format(bell(-10,35)))
	estimate = x*samplertt[counter]*y
	estimate = 40.0 if estimate<40 else estimate
	estimate = 6000 if estimate>6000 else estimate
	estimate = float("{0:.3f}".format(estimate))
	samplertt.append(estimate)
	counter+=1
	return samplertt,counter

def dostuff(samplertt,counter):
	ring = float("{0:.3f}".format(bell(0,1)))
	if ring<=0.25:
		temp = 40.0 if 1.85*samplertt[counter]<40 else 1.85*samplertt[counter]
		temp = 6000 if temp>6000 else temp
		temp = float("{0:.3f}".format(temp))
		samplertt.append(temp)
		counter+=1
	elif ring <=0.5:
		temp = 40.0 if 0.65*samplertt[counter]<40 else 0.65*samplertt[counter]
		temp = 6000 if temp>6000 else temp
		temp = float("{0:.3f}".format(temp))
		samplertt.append(temp)
		counter+=1
	elif ring<= 0.75:
		temp2 = 40.0 if 1.6*samplertt[counter]<40 else 1.6*samplertt[counter]
		temp2 = 6000 if temp2>6000 else temp2
		temp2 = float("{0:.3f}".format(temp2))
		samplertt.append(temp2)
		counter+=1
		if counter+1 <200:
			temp3 = 40.0 if 0.7*samplertt[counter]<40 else 0.7*samplertt[counter]
			temp3 = 6000 if temp3>6000 else temp3
			temp3 = float("{0:.3f}".format(temp3))
			samplertt.append(temp3)
			counter+=1
	else:
		(samplertt,counter) = normalestimation(samplertt,counter)
	return samplertt,counter

def roundtriptimes():
	samplertt=[]
	samplertt.append(100) # this is the initial value
	counter = 0
	while counter<199:
		if counter<19:
			(samplertt,counter) = normalestimation(samplertt,counter)
		else:
			if counter%5==0:
				(samplertt,counter) = dostuff(samplertt,counter)
			else:
				(samplertt,counter) = normalestimation(samplertt,counter)

	return samplertt

def EstimateRTT(samplertt,a):
	Estimatertt = []
	Estimatertt.append(100)
	for i in range(len(samplertt):
		temp = (1-a)Estimatertt[i] + a*samplertt[i]
		Estimatertt.append(temp)
	return Estimatertt

def Devrtt(samplertt,estimatertt,b):
	devrtt = []
	devrtt.append(100)
	for i in range(len(samplertt)):
		temp = (1-b)devrtt[i] + b*abs(samplertt[i]-estimatertt[i])
		devrtt.append(temp)
	return devrtt

def timeoutintervals(estimatertt,devrtt):
	lst = []
	for i in len(estimatertt):
		lst.append(estimatertt[i]+4*devrtt[i])
	return lst
	
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

B = [0.125,0.375]
A = [0.4,0.25]
