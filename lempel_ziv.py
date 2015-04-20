dictionary=[]
Prefix=""
source=raw_input("Please state the name of the file you'd like to encode: ")
try:
	f=open(source,"r")
except IOError as e:
	print 'The file you typed does not exist!'
   
out=open("encodedfile.txt","w")
ite=f.read(1)

while(ite!=""):
	temp=ite+Prefix
	if (temp in dictionary):
		Prefix=Prefix+ite
	else:
		if(Prefix==""):
			CWP=0
		else:
			CWP=dictionary.index(Prefix)+1
			out.write(CWP)
			out.write(ite)
			dictionary.append(temp)
			Prefix=""
	ite=f.read(1)

if(Prefix!=""):
	CWP=dictionary.index(Prefix)+1
	out.write(CWP)
	
out.close()
f.close()
