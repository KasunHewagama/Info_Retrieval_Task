# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:23:35 2020

@author: Kasun_Hewagama
@Sid: IT18165180
@Batch: DS 2020
"""
#Question 1 Answer...!

#Initializing lists and dictionaries
listSet2 = []
bag_Of_Words = []
word_Matrix = []
Posting_List = []
Term_Dictionary = {}

#Reading Documents one by one and get the input
#In Q2 I take whole files as once for the input
#Because of that i took mone file by one in here
with open('Q1_Docs/Document1.txt', 'r') as f:
    Document1 = f.read().lower().replace(".", "").split(" ")

with open('Q1_Docs/Document2.txt', 'r') as f:
    Document2 = f.read().lower().replace(".", "").split(" ")

with open('Q1_Docs/Document3.txt', 'r') as f:
    Document3 = f.read().lower().replace(".", "").split(" ")

#Adding 3 read files to a single document
Documents= [Document1,Document2,Document3]
bag_Of_Words = Document1 + Document2 + Document3

#Adding one word by one for the posting list
for word in bag_Of_Words:
    if word in Posting_List:
        continue
    else:
        Posting_List.append(word)

#Adding one word by one for the word matrix from the posting list
for word in Posting_List:
    row_add = []
    for doc in Documents:
        if word in doc:
            row_add.append(1)
        else:
            row_add.append(0)
    word_Matrix.append(row_add)

#Output the posting list as Docuent Term Matrix
print("\n Term Document Matrix For Document1 & Document2 & Document3...!\n")
for i in range(0, len(word_Matrix)):
    Term_Dictionary[Posting_List[i]] = word_Matrix[i]
    print(" -- " + Posting_List[i] + " => " + str(word_Matrix[i]) + " -- ")
   

#Creating AND operation to get the output as mentioning in the Assignmnet
def AND_Operation(listSet1, listSet2, listSet3):
    return_List = []
    for k in range(len(listSet1)):
        if listSet1[k] == 1 and listSet2[k] == 1 and listSet3[k] == 1:
            document = 'Document' + str(k+1)
            return_List.append(document)
    return return_List

#Taking the lsited items in Assignment from document term dictionary
def get_listed(word):
    return Term_Dictionary[word]

#Taking the not lsited items in Assignment from document term dictionary
def get_not_listed(word):
    listSet1 = Term_Dictionary[word]
    for j in range(len(listSet1)):
        if listSet1[j] == 0:
            listSet2.append(1)
        else:
            listSet2.append(0)
    return listSet2


print("\n--Documents Identified by Document Term Matrix--\n")
#Outputting Suitable answers for the Question_1 and Question_2
Q1_rslt = AND_Operation(get_listed('frodo'), get_listed('orc'), get_listed('sword'))
Q2_rslt = AND_Operation(get_listed('sam'), get_listed('blue'), get_not_listed('frodo'))    

print("(Frodo AND orc AND sword) => " + str(Q1_rslt)) 
print("(Sam AND blue AND NOT Frodo) => " + str(Q2_rslt))

print("\n-------------------------------------------------\n")