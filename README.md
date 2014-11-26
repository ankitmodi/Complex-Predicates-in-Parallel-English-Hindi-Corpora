Complex-Predicates in Parallel English-Hindi Corpus
==================
This project was done by Amit Kumar and Ankit modi in course Natural Language Processing (CS671) under the guidance of Prof. Amitabha Mukerjee. For more details see the project report enclosed. 

Required Resources ::
This project needs a parallel alinged copora of Hindi-English sentences.
(You can get one corpora we used from this link : nsfannsf 
You also need python for running scripts written in python.



Files Present : 
1. lightVerb_detection.py - Detects Complex Predicates from corpora using LightVerb.txt, EnglishForms.txt and HindiForms.txt. Outputs the output.txt file.
2. count_LV.py - Contains python code which take output.txt as input and gives light_verbs_calculated.txt as output.
3. LightVerb.txt - Contains a list of all Light Verbs in Hindi and their corresponding English meanings.
4. HindiForms.txt - Contains lists of Light Verbs and their forms.
5. EnglishForms.txt - Contains list of forms of all english meanings of Light Verbs present in LightVerb.txt 
6. light_verb_freq.txt - Contains the frequencies of all basic form of Light Verbs that are used in corpora.
7. light_verbs_calculated.txt - Contains a list of all unique Light Verbs in their base form detected from corpora.
8. en.train.tok - English counterpart of the aligned dataset.
8. hi.train.tok - Hindi counterpart of the aligned dataset.
9. output.txt - Contains a list of all detected Complex Predicates from given corpora.



APPROACH DETAILS ::
1. We first made list of all Light Verbs in Hindi and their corresponding english meaning (LightVerb.txt). 
2. Then make a list of all forms of Light Verbs mentioned in LightVerb.txt .
3. Make a list of all forms of english meaning of Light Verbs.
4. Make a list of all forms of Light Verbs in Hindi.
5. Run lightVerb_detection.py on parallel corpora to get list of all Complex predicates present in the corpora (output.txt).
	Use this command for running lightVerb_detection.py : 
	>> python lightVerb_detection.py
6. Run count_LV.py on output.txt which gives light_verbs_calculated.txt.
	Run this command for running count_LV.py :
	>> python count_LV.py
7. Run this command for getting frequencies of all Light Verbs detected from corpora.
	>> sort < light_vers_calculated.txt | uniq -c | sort -nr > light_verb_freq.txt




