word1 = raw_input("Please insert the first word: ")
word2 = raw_input("Please insert the second word: ")

binarylist1 = [format(ord(letter),'08b') for letter in word1] # me list conprehension pernaw oles tis duadikes times twn stoixeiwn tou string se lista
binarylist2 = [format(ord(letter),'08b') for letter in word2] 

diff1 = len(binarylist1)
diff2 = len(binarylist2)

counter = 0 #metritis pou metraei tis diafores twn bit
if diff1>diff2:
	new = diff1 - diff2
	for i in range(new):
		binarylist2.append(format(0,'08b'))
elif diff2>diff1:
	new = diff2-diff1
	for i in range(new):
		binarylist1.append(format(0,'08b'))

for x,y in zip(binarylist1,binarylist2):
	for i in range(8):
		if x[i]!=y[i]:
			counter+=1

print "the words differ by %d bits"%counter	
