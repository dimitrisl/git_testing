import random

def elegxos(psifia,to_test):
	counter = 0
	for i in range(1,11):
		if pow(i,to_test,to_test)==i:
			counter+=1 #tsekarw ton arithmo an pernaei deka fores to test
	if counter==10:
		print "%d is a prime number"%to_test
		return to_test
	else:
		to_test = 0
		return to_test


psifia = input("State the number of digits: ")

while psifia <=0 :
	psifia = input("Please enter a valid ammount of digits : ")

if psifia==1:
	print random.choice([1,3,5,7])
else:	
	arxi = 10**(psifia-1)
	telos = 10**(psifia)
	result = ""
	testarisma = random.randint(arxi,telos)
	while arxi<=telos:
			result = elegxos(psifia,testarisma)
			if result !=0:
				break
			else:
				testarisma = random.randint(arxi,telos)
				
stop = raw_input("\n'Press any key to close this. '")
