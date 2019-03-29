#Требования к исходному файлу: первый столбец — Lexeme, остальные — по языкам. Желательно, чтобы языки были в алфавитном порядке (для одной из следующих программ это обязательно). 
#счётчик == 1
#идём по строчкам файла
#генерируем элемент словаря — массив
#если счётчик есть в ячейке — ставим 1 в массив в словаре, если нет — ставим 0, если NA — ставим NA
#увеличиваем счётчик

import sys, re
table = []
for line in sys.stdin.readlines():
	table.append(line.strip("\r\n")) 

source_wordlist = {}
for line in table[1:]:
	a = line.split("\t")
	source_wordlist[a[0]] = a[1:]

res_wordlist = {}

#finding maximum for each line
line_max = {}
for entry in source_wordlist:
	if entry == "Speaker":
		continue
	#print(entry)
	numbers_in_line = []
	for element in source_wordlist[entry]:
		numbers_in_line.extend(element.split(" "))
	n = []
	for number in numbers_in_line:
		if number != "NA":
			#print(number)
			n.append(int(number))
	n.sort()
	entry_max = n[len(n)-1]
	line_max[entry] =  int(entry_max)
	#print(line_max[entry])

res_wordlist = {}
for entry in source_wordlist:
	counter = 1
	lexeme_d = {}
	while counter <= line_max[entry]:
		lexeme_arr = []
		for word in source_wordlist[entry]:
			current_set = word.split(" ")
			for i in range(len(current_set)):
				if current_set[i] != "NA":
					current_set[i] = int(current_set[i])
			if counter in current_set:
				lexeme_arr.append("1")
			elif word == "NA": 
				lexeme_arr.append("NA")
			else:
				lexeme_arr.append("0")
			if "1" in lexeme_arr:
				lexeme_d[counter] = lexeme_arr
		counter += 1
	res_wordlist[entry] = (lexeme_d)
#print(res_wordlist)	

#res_table = "Lexeme;Similarity_Set;Dict_Rutul;Rutul_Rutul_Vera;Ikhrek_Rutul_Jariyat;Ikhrek_Rutul_Aishe;Ikhrek_Rutul_Zijawudin;Ikhrek_Rutul_Salimat;Kina_Rutul_Nurulla;Kina_Rutul_Mevletdin;Kina_Rutul_Magomed-Shapi;Kiche_Rutul_Serazhudin;Kiche_Rutul_Sejfulla;Dict_Azer;Dict_Kumyk;Dict_Lezgian\r\n"
title = ""
for element in table[0].split("\t")[1:]:
	title += "\t"+element 
title = "Lexeme" + title
res_table = title+"\r\n"
for entry in res_wordlist:
	for set in res_wordlist[entry]:
		s = ''
		for element in res_wordlist[entry][set]:
			s += str(element)+"\t"
		s = s.strip("\t")
		res_table += entry+"_"+str(set)+"\t"+s+"\r\n"
res_table = re.sub(" ","_",res_table)
res_table = res_table.strip("\n")
print(res_table)
