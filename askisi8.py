f = open('prakseis.txt')
list_of_txt = f.readlines()

sanitize = [ i[:-1] for i in list_of_txt]

results = []

for i in sanitize:
	operator = ""
	for element in i:
		if not element.isdigit():
			operator+= element
	token = i.split(operator)
	first = int(token[0])
	second = int(token[1])
	if operator == "*":
		results.append(first*second)
	elif operator == "/":
		results.append(first/second)
	elif operator == "**":
		results.append(first**second)
	elif operator == "+":
		results.append(first+second)
	elif operator == "-":
		results.append(first-second)
	
for (x,y) in zip(range(len(sanitize)),sanitize):
	print y," = ",results[x]

f.close()

