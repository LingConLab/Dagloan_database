#0 - concept - 4, 2 - speaker - 0, 4 - word - 6
import sys, re
table = []
metatable = []
metadata = {}
metafile = open('meta_01042019.tsv', 'r')

def subst(pattern, subst, string):
	while(pattern in string):
		string = re.sub(pattern, subst, string)
	return string


for line in metafile:
	metatable.append(line.strip("\r\n")) 
for line in metatable[1:]:
	a = line.split("\t")
	metadata[a[4]] = a[0]
		
for line in sys.stdin.readlines():
	table.append(line.strip("\r\n")) 
meaninglist = {}
#speaker_list = table[4].split("\t")[1:]

#For Speaker as a column:
#for line in table[1:]:
#	a = line.split("\t")
#	if a[4] in meaninglist and a[0] in meaninglist[a[4]]:
#		meaninglist[a[4]][a[0]].append(a[6])
#	elif a[4] in meaninglist and a[0] not in meaninglist[a[4]]:
#		meaninglist[a[4]][a[0]] = [a[6]]
#	else:
#		meaninglist[a[4]] = {a[0]:[a[6]]}

#For Speaker as a row:
for line in table[1:]:
	a = line.split("\t")
	if a[0] in meaninglist and a[4] in meaninglist[a[0]]:
		meaninglist[a[0]][a[4]].append(a[6])
	elif a[0] in meaninglist and a[4] not in meaninglist[a[0]]:
		meaninglist[a[0]][a[4]] = [a[6]]
	else:
		meaninglist[a[0]] = {a[4]:[a[6]]}
		
#print(meaninglist)

#For Speaker as a column:
#header = 'Lexeme\t'
#result = '\n'
#used_ids = set()
#for concept in meaninglist:
#	result += str(concept) + "\t"	
#	for speaker in metadata:			
#		#header += str(metadata[speaker]) + "\t"
#		if speaker not in used_ids:
#			header += str(metadata[speaker]) + "\t"
#			used_ids.add(speaker)
#		#result += str(meaninglist[speaker][concept]) + "\t"
#		if speaker in meaninglist[concept]:
#			for word in meaninglist[concept][speaker]:
#				result += str(word) + " "
#			result += "\t"
#		else:
#			result += "NA\t"
#	result += "\n"

#For Speaker as a row:
header = 'Speaker\t'
result = '\n'

for speaker in sorted(meaninglist):
	result += speaker + "\t"
	for concept in meaninglist[speaker]:
		if str(concept) not in header:
			header += str(concept) + "\t"
		#result += str(meaninglist[speaker][concept]) + "\t"
		for word in meaninglist[speaker][concept]:
			result += str(word) + " "
		result += "\t"
	result += "\n"

#result = header + result
#print(result)

			
result = header + result


result = subst("NA ", "", result)
result = subst(" NA", "", result)
result = subst("\t\t", "\tNA\t", result)
result = subst("\t\t", "\tNA\t", result)
result = subst("\t\n", "\n", result)
result = subst(" \n", "\n", result)
result = subst(" \t", "\t", result)
result = subst("\t ", "\t", result)
result = result.strip("\n")

print(result)