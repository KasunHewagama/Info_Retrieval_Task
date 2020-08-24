# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:30:54 2020

@author: Kasun_Hewagama
@Sid: IT18165180
@Batch: DS 2020
"""


import os
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

with open('Stopwords.txt') as f:
    for line in f:
        stopwords = line.split(", ")
#print stopwords

tokens = {}
porter = PorterStemmer()
documentID = 0
#path = r"C:/Users/user/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/Assignment_1/Q1_Docs"
#path = r"C:/Users/user/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/week 3/Docs"
path = r"C:/Users/user/AppData/Roaming/nltk_data/corpora/reuters/training"


# sent = sent_tokenize(lower_new_text)
# for s in sent:
#     print(wordnet.lemmatize(s) if wordnet.lemmatize(s).endswith('e') else porter.stem(s))


# words = word_tokenize(lower_new_text)
# for w in words:
#     print(wordnet.lemmatize(w) if wordnet.lemmatize(w).endswith('e') else porter.stem(w))




for root, dirs, files in os.walk(path):
    for file in files:
        with open(os.path.join(path, file)) as f:
                documentID += 1
                line_tokens = []
                for line in f:
                    line_tokens = line.split(  )
                    for each in line_tokens:
#                        if each[-1] in [',','!','?','.','>',' ','"',')',"'",'']:
#                            each = each[:-1]
#                        if each[-2] in [',','!','?','.','>',' ','"',')',"'",'']:
#                            each = each[:-1]

                        each = "".join(u for u in each if u not in ('+',"?",',','<','>','{','}','-','_','$','&', ".", ";", ":", "!",'"',"'",' ',')','(','[',']'))
                        if each not in stopwords:
                            each = porter.stem(each)                            
                            if each not in tokens:
                                tokens[each.replace(".","").lower()] = [documentID]
                            else:
                                tokens[each].append(documentID)

file = open("InvertedIndex.txt", "w")
for key in sorted(tokens):
    file.write(key)
    file.write(" => ")
    value = ','.join(str(v) for v in tokens[key])
    file.write(value)
    file.write("\n")
file.close()


