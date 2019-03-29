import sys, re
table = []
metatable = []
metadata = {}
metafile = open('meta_28032019.tsv', 'r')

def subst(pattern, subst, string):
	while(pattern in string):
		string = re.sub(pattern, subst, string)
	return string


for line in metafile:
	metatable.append(line.strip("\r\n")) 
for line in metatable[1:]:
	a = line.split("\t")
	metadata[a[2]] = str(a[3]) + "\t" + str(a[5]) + "\t" + str(a[9]) # Language, Village, District

for line in sys.stdin.readlines():
	table.append(line.strip("\r\n")) 
meaninglist = {}
#speaker_list = table[0].split("\t")[1:]

header = table[0].split("\t")
speakerlist = {}
for i in range(1,len(header)-1):
	speakerlist[header[i]] = {}
	for line in table[1:]: 
		speakerlist[header[i]][line.split("\t")[0]] = line.split("\t")[i]
		
#print(meaninglist)

header = 'Speaker\tLanguage\tVillage\tDistrict\t'
result = '\n'
used_ids = set()
for speaker in speakerlist:
	result += speaker+ "\t" + str(metadata[speaker]) + "\t"
	for lexeme in speakerlist[speaker]:
		if str(lexeme) not in header:
			header += str(lexeme) + "\t"
		#result += str(meaninglist[speaker][concept]) + "\t"
		for word in speakerlist[speaker][lexeme]:
			result += str(word) + " "
		result += "\t"
	result += "\n"

result = header + result
#print(result)

			
#result = header + result


result = subst("N A", "NA", result)
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