import sys, os
os.chdir("/Users/ilchec/Documents/Uni/DagLoans/Dagloan_database")
f1 = open("words_21012019.csv")
f2 = open("words_s05022019.csv")
#f1 = open("ilia500.csv")
#f2 = open("samira500.csv")

table1 = []
table2 = []
for line in f1:
	table1.append(line.strip("\r\n")) 
for line in f2:
	table2.append(line.strip("\r\n"))
wordlist1 = {}
wordlist2 = {}
for line in table1[1:]:
	a = line.split("\t")
	if a[4].isdigit() == True:
		#current_word = a[1]+"\t"+a[3]
		current_word = a[0]+"\t"+a[1]+"\t"+a[3]
		current_set = a[0]+"\t"+a[1]+"\t"+a[4]
		wordlist1[current_word] = set()
		for l in table1[1:]:
			b = l.split("\t")
			if b[0]+"\t"+b[1]+"\t"+b[4] == current_set:
				wordlist1[current_word].add(b[3])
for line in table2[1:]:
	a = line.split("\t")
	if a[4].isdigit() == True:
		current_word = a[0]+"\t"+a[1]+"\t"+a[3]
		current_set = a[0]+"\t"+a[1]+"\t"+a[4]
		wordlist2[current_word] = set()
		for l in table2[1:]:
			b = l.split("\t")
			if b[0]+"\t"+b[1]+"\t"+b[4] == current_set:
				wordlist2[current_word].add(b[3])
similar_sets = 0
different_sets = 0
list_differences = 0
s = "Meanint\tMeaning_ID\tWord\tList1\tList2\tSimilarity\n"
for word in wordlist1:
	if word in wordlist2:
		if wordlist1[word] ==  wordlist2[word]:
			similar_sets += 1
			#print(str(wordlist1[word])+"\t"+str(wordlist2[word])+ "\t" + "SIMILAR")
		else:
			different_sets += 1
			if str(wordlist1[word])+"\t"+str(wordlist2[word])+ "\t" + "DIFFERENT" not in s:
				s += (str(word)+"\t"+str(wordlist1[word])+"\t"+str(wordlist2[word])+ "\t" + "DIFFERENT\n")
	else:
		list_differences += 1
		if (str(wordlist1[word])+"\t\t"+"NOT IN LIST 2") not in s:
			s += (str(word)+"\t"+str(wordlist1[word])+"\t\t"+"NOT IN LIST 2\n")
for word in wordlist2:
	if word in wordlist2:
		continue
	else:
		list_differences += 1
		if (str(wordlist1[word])+"\t\t"+"NOT IN LIST 1") not in s:
			s += (str(word)+"\t"+str(wordlist1[word])+"\t\t"+"NOT IN LIST 1")
print(s)
			
	