# -*- coding: utf-8 -*-

##### THis File counts the Number of all unique Light Verbs in their base form detected.
##### It takes file which contains list of all complex predicates detected from corpora.
##### Gives list of all unique Light Verbs used in corpora.
import re, collections
import codecs

inpu =  codecs.open('output.txt','r','utf-8')
out =  codecs.open('light_vers_calculated.txt','w','utf-8')

lv_set = []			## list of all unique LVs
light_verbs = []
for LV in inpu:
	light_v = LV.split(' ')
	if(len(light_v) > 1):				## in case there is only one word in complex predicat ( if LV is first word of sentence
	#	print >> out ,light_v[1].rstrip()
		f =  codecs.open("HindiForms.txt", 'r','utf-8')
		for line in f:						## find the base form of LV detected. 
			light_ver = line.split(", ")
			if light_v[1].rstrip() in light_ver:
				print >> out,light_ver[0] 
				break 
	

	#if not (light in light_verbs):
	#	light_verbs.append(light)
	#print "pre word is : " + pre
	#print "light verb is : " + light
	if not (LV in lv_set):					## Computing list of unique LVs
		lv_set.append(LV)
	

print len(lv_set)
