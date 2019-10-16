#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:29:15 2019

@author: manyu
"""

import numpy as np
import tensorflow as tf
import re
import time

print("hello")

lines=open("movie_lines.txt", encoding="utf-8", errors="ignore").read().split("\n")
movie_convesation=open("movie_conversations.txt", encoding="utf-8", errors="ignore").read().split("\n")

id2line={}

###creating a dictionary that maps each line and its id
for line in lines:
   _line=line.split(' +++$+++ ')
   if len(_line)==5:
       id2line[_line[0]]=_line[4]
       
### creating list of all conversations
conversation_ids=[]
for conversation in movie_convesation[:-1]:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","") 
    conversation_ids.append(_conversation.split(','))     
    
 
###getting seperately the question and the answers    
questions=[]
answers=[]
for conversation in conversation_ids:
    for i in range(len(conversation)-1):
        questions.append(id2line[conversation[i]])
        answers.append(id2line[conversation[i+1]])
        
        
        
#Doing a first cleaning of texts
def clean_text(text):
    text=text.lower()
    text=re.sub(r"i'm","i am",text)  
    text=re.sub(r"he's","he is",text)
    text=re.sub(r"she's","she is",text) 
    text=re.sub(r"that's","that is",text)  
    text=re.sub(r"what's","what is",text)   
    text=re.sub(r"where's","where is",text)
    text=re.sub(r"\'ll","will",text)
    text=re.sub(r"\'ve","have",text)
    text=re.sub(r"\'re","are",text)
    text=re.sub(r"\'d","would",text)
    text=re.sub(r"won't","will not",text)
    text=re.sub(r"can't","cannot",text)
    text=re.sub(r"[-()\"#/@;:<>{}+=|.?,]","",text)
    return text

###cleaning question
clean_question=[]
for question in questions:
    clean_question.append(clean_text(question))


### cleaning answers               
clean_answers=[]
for answer in answers:
    clean_answers.append(clean_text(answer))  



##### creating a ditionary  that maps each word its number of occurances
word2count={}
for question in clean_question:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1

for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] += 1
