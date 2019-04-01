import sys, re, operator
table = []
metatable = []
metadata = {}
names = {}
metafile = open('meta_01042019.tsv', 'r')

def subst(pattern, subst, string):
	while(pattern in string):
		string = re.sub(pattern, subst, string)
	return string


for line in metafile:
	metatable.append(line.strip("\r\n")) 
for line in metatable[1:]:
	a = line.split("\t")
	metadata[a[0]] = a[1]
for line in metatable[1:]:
	a = line.split("\t")
	names[a[0]] = a[2]		
for line in sys.stdin.readlines():
	table.append(line.strip("\r\n")) 
meaninglist = {}
#speaker_list = table[0].split("\t")[1:]

#For Speaker as a column:
transcription_frequency = {}
for line in table[1:]:
	a = line.split("\t")
	if str(a[0])+" "+str(a[4]) in transcription_frequency:
		if a[3] in transcription_frequency[str(a[0])+" "+str(a[4])]:
			transcription_frequency[str(a[0])+" "+str(a[4])][a[3]] += 1
		else:
			transcription_frequency[str(a[0])+" "+str(a[4])][a[3]] = 1
	else:
		transcription_frequency[str(a[0])+" "+str(a[4])] = {}
		transcription_frequency[str(a[0])+" "+str(a[4])][a[3]] = 1

good_transcriptions = {}
for line in table[1:]:
	a = line.split("\t")
	good_transcriptions[str(a[0])+" "+str(a[4])] = ""

for line in table[1:]:
	a = line.split("\t")
	if "D" in metadata[a[2]]:
		good_transcriptions[str(a[0])+" "+str(a[4])] += a[3] + " (" + names[a[2]][2:] + " Dictionary); "

for element in good_transcriptions:
	good_transcriptions[element] += max(transcription_frequency[element].items(), key=operator.itemgetter(1))[0] + " (Frequency); "

#assigning dict IDs
#for line in table[1:]:
#	a = line.split("\t")
#	if str(a[0])+" "+str(a[4])

#For Speaker as a row:
#for line in table[1:]:
#	a = line.split("\t")
#	if a[2] in meaninglist and a[0] in meaninglist[a[2]]:
#		meaninglist[a[2]][a[0]].append(a[4])
#	elif a[2] in meaninglist and a[0] not in meaninglist[a[2]]:
#		meaninglist[a[2]][a[0]] = [a[4]]
#	else:
#		meaninglist[a[2]] = {a[0]:[a[4]]}
		
#print(meaninglist)

#For Speaker as a column:
result = ""
for line in table[1:]:
	a = line.split("\t")
	for element in a:
		result += str(element)+"\t"
	result = result + good_transcriptions[str(a[0])+" "+str(a[4])].strip("; ")+"\n"

header = ""
for element in table[0].split("\t"):
	header += element + "\t"
header += "Standardized Transcription\n"
result = header + result	

#For Speaker as a row:
#header = 'Speaker\t'
#result = '\n'
#for speaker in meaninglist:
#	result += str(metadata[speaker]) + "\t"
#	for concept in meaninglist[speaker]:
#		if str(concept) not in header:
#			header += str(concept) + "\t"
#		#result += str(meaninglist[speaker][concept]) + "\t"
#		for word in meaninglist[speaker][concept]:
#			result += str(word) + " "
#		result += "\t"
#	result += "\n"
#
#result = header + result
#print(result)

			


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