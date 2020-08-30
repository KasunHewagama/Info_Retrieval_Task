# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:30:54 2020

@author: Kasun_Hewagama
@Sid: IT18165180
@Batch: DS 2020
"""
import os
import nltk
from nltk.stem import PorterStemmer

cwd = os.getcwd()
documentID = []


porter = PorterStemmer() #For Stemming
#For Sentence Tokanization
#For Word Tokanization


#Accessing the files from location
#For testing purposes I used these locations and these contain Question 1 documents.
path = "C:/Users/KasunHewagama/AppData/Roaming/nltk_data/corpora/reuters/training"
#path = r"C:/Users/KasunHewagama/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/week 3/Docs"
#path = 'C:/Users/KasunHewagama/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/Assignment_1/Q1_Docs'

os.chdir(path)
accessFileList =os.listdir(os.getcwd())

for root, dirs, files in os.walk(path):
    for file in files:
        with open(os.path.join(path, file)) as f:
            documentID.append(f.read())


#   Question 1 Sub part 1 Starting
#Build modules to tokenize words and sentences.	
            
#concatanate words in a single file
concatanate_Words = []
#concatanate Sentences in a single file
concatanate_Sentences = []
#taking file by file to concatanate words
for lines in documentID:
    wordLine = nltk.sent_tokenize(lines)
    concatanate_Sentences.append(wordLine)
    for word in wordLine:
        tokenizedWord = nltk.word_tokenize(word)
        concatanate_Words.append(tokenizedWord)


#passing all the words to assign unique value or a token
#Goes through document by document
line_tokens = []
for line in concatanate_Words: #Goes throught line by line
    for each in line: 
        if each in line_tokens: #Seacrching new tokens
            continue
        else: #if found adding them
            line_tokens.append(each)
#print(line_tokens)

            
#   Question 1 Sub part 1 Ending


#   Question 1 Sub part 2 Starting
#Build module for Porter Stemmer to do stemming
stemmer = []            
for each in line_tokens:
    stemmer.append(porter.stem(each))
#print(stemmer)


#   Question 1 Sub part 2 Ending
   
    
#   Removing Stopwords are necessary while it comes to Info.Retrival

#Deallocating stopWords which are in the stopword.txt file
with open('C:/Users/KasunHewagama/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/Assignment_1/Stopwords.txt') as f:
    for line in f:
        stopwords = line.split(",")
        stopWordRemover = []
        for each in stemmer:
            if each in stopwords:
                continue
            else:
                stopWordRemover.append(each)
#print(stopWordRemover)
        
        
#Deallocating the characters indicating in the below to output better resultset        
character_Remover = ['..','+',"?",',','<','>','{','}','-','_','$','&', ".", ";", ":", "!",'"',"'",' ',')','(','[',']']
        
tokener = []
for each in stopWordRemover:
    if each in tokener or each in character_Remover:
        continue
    else:
        tokener.append(each)
#print(tokener)


    
#   Question 1 Sub part 3 Starting
#Build module to apply case folding i.e. convert words to lower case. 
FinalDict = []
for each in stopWordRemover:
    #changing uppercase ltrs to lowercase ltrs
    FinalDict.append(each.lower())

#   Question 1 Sub part 3 Ending

#   Question 1 Sub part 4 Starting      
#Build inverted index and posting list as python dictionary    
Inv_Ind_Post_list = {}    
for each in FinalDict:
    All_Document_List = []
    for root, dirs, files in os.walk(path):
        for file in files:
            with open(os.path.join(path, file)) as f:
                just_In_Use = f.read()
                if each in just_In_Use:
                    All_Document_List.append(str(file))
        Inv_Ind_Post_list[each] = All_Document_List
      

#Printing invertedIndex file as text file in same folder
os.chdir('C:/Users/KasunHewagama/Desktop/SLIIT/Year 3/Semester 2/IRWA-IT3041/Assignment_1') 
fileEnd = open("InvInd.txt", "w")
for key, value in sorted(Inv_Ind_Post_list.items()):
    fileEnd.write(key + "  -->  " +str(value) + " \n")
#     file.write(" => ")
#     value = ','.join(str(v) for v in tokens[key])
#     file.write(value)
#     file.write("\n")
fileEnd.close()

#   Question 1 Sub part 4 Ending 


#   Question 1 Sub part 5 Starting
#Build a generalized module to merge any number of posting lists
def post_list_Adding(each_Word):
    length_line = len(each_Word)
    prime_word = each_Word[0]
    line_Ret = []
    
    if length_line == 1:
        line_Ret = Inv_Ind_Post_list[prime_word]
        return line_Ret
    
    for k in range(1, length_line):
        if k == 1:
            line_Ret = set(Inv_Ind_Post_list[prime_word]).intersection(Inv_Ind_Post_list[each_Word[k]])
        else:
            line_Ret = set(line_Ret).intersection(Inv_Ind_Post_list[each_Word[k]])
    return line_Ret

#
merge = ['blue', 'lamp', 'locat']
print("Your Result is \n"+str(post_list_Adding(merge)))
#   Question 1 Sub part 5 Ending
