import sys
table = []
for line in sys.stdin.readlines():
	table.append(line.strip("\n")) 

d = {}
for i in table[1:]:
	d[i.split("	")[0]] = []
	for j in table[1:]:
		diss = 0
		divider = 0
		arr1 = i.split("	")[1:]
		arr2 = j.split("	")[1:]
		for k in range(len(arr1)):
			element1 = arr1[k]
			element2 = arr2[k]
			common = list(set([c for c in element2.split(" ") if c in element1.split(" ")]))
			if len(common) == 0 and "NA" not in element1 and "NA" not in element2:
				diss += 1
				divider += 1
			elif "NA" not in element1 and "NA" not in element2:
				 divider += 1
		if divider == 0:
			divider += 1
		dist = diss/divider
		d[i.split("	")[0]].append({j.split("	")[0]:dist})

		
#for element in sorted(d):
#	print(str(element) + " 	 " + str(d[element]) + "\r\n")

#print(d)
s = "Speaker\t"
for element in sorted(d):
	s += str(element)
	s += "	"
	
s = s.strip("	")
s += "\r\n"
for element in sorted(d):
	s += str(element)
	s += "	"
	for item in d[element]:
		for i in sorted(item):
			s += str(item[i])
			s += "	"
	s = s.strip("	")
	s += "\r\n"	
print(s)
	