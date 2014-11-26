#!/usr/bin/python

# -*- coding: utf-8 -*-
import codecs


light_verb_list = []
light_verb_root_list =[]
#f = codecs.open("HindiForms.txt", 'r', 'utf-8')


### Make a list of all light verbs and their forms.
f = open("HindiForms.txt", 'r')
for line in f:
	light_verb = line.split(", ")
	for item in light_verb:
		light_verb_list.append(item)
		light_verb_root_list.append(light_verb[0])
f.close()


f1 = open("output.txt", 'w')
#for item1, item2 in zip(light_verb_list, light_verb_root_list):
#	f1.write(item2 + "	" + item1 + "\n")
		




## Make a list of all LVs in base form and their english meanings.
root_word_list = []
eng_root_word_list = []
f_root = open("LightVerb.txt", 'r')
for line in f_root:
	root_verb = line.split("		")
	root_word_list.append(root_verb[0])
	eng_root_word_list.append(root_verb[1])


#for item1, item2 in zip(root_word_list, eng_root_word_list):
#	f1.write(item1 + "	" + item2)

eng_word_form1 = []
eng_word_form2 = []
eng_word_form3 = []
eng_word_form4 = []
eng_word_form5 = []


## Make lists of forms of English meaning of LVs.
f_eng_word = open("EnglishForms.txt", 'r')
for line in f_eng_word:
	verb_forms = line.split("	")
	eng_word_form1.append(verb_forms[0])
	eng_word_form2.append(verb_forms[1])
	eng_word_form3.append(verb_forms[2])
	eng_word_form4.append(verb_forms[3])
	eng_word_form5.append(verb_forms[4])
#for item1, item2, item3,item4, item5 in zip(eng_word_form1, eng_word_form2, eng_word_form3, eng_word_form4, eng_word_form5):
#	f1.write(item1 + item2+ "	" + item3+ "	" + item4+ "	" + item5 + "\n")










#f_eng = open("etest.txt")
#f_hindi = open("htest.txt")
#f_eng = open("english_test.txt")
#f_hindi = open("hindi_test.txt")
f_eng = open("en.train.tok")
f_hindi = open("hi.train.tok")


#### ALGORITHM FOR COMPLEX PREDICATE DETECION

words_hin = []
words_eng = []
for line1, line2 in zip(f_hindi, f_eng):
	#f1.write("\n")
	words_hin = line1.split(" ")
	words_eng = line2.split(" ")

	for item in words_hin:
		if item in light_verb_list:
			idx = light_verb_list.index(item)
			sen_idx = words_hin.index(item)
			root_verb = light_verb_root_list[idx]
			
			if root_verb in root_word_list:
				idx2 = root_word_list.index(root_verb)
				eng_root = eng_root_word_list[idx2][:-1]
				#f1.write(item + ' ' + root_verb + ' '  + eng_root + "\n")
				if eng_root in eng_word_form1:
					idx3 = eng_word_form1.index(eng_root)
					#f1.write(item + ' ' + root_verb + ' '  + eng_root + ' ' + eng_word_form1[idx3] + ' ' + eng_word_form2[idx3] + ' ' + eng_word_form3[idx3] + ' ' + eng_word_form4[idx3] + ' ' + eng_word_form5[idx3] + "\n")

					t1 = eng_word_form1[idx3]
					t2 = eng_word_form2[idx3]
					t3 = eng_word_form3[idx3]
					t4 = eng_word_form4[idx3]
					t5 = eng_word_form5[idx3]

					if t1 in words_eng:
						pass
					elif t2 in words_eng:
						pass
					elif t3 in words_eng:
						pass
					elif t4 in words_eng:
						pass
					elif t5 in words_eng:
						pass
					else:
						verb_before = words_hin[sen_idx - 1]
						f1.write(verb_before + " " + item + "\n")
	
		else:
			pass


