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

###
for line in lines:
   _line=line.split(' +++$+++ ')
   if len(_line)==5:
       id2line[_line[0]]=_line[4]
       

conversation_ids={}
for conversation in movie_convesation[:-1]:
    _conversation = movie_convesation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","") 
    conversation_ids.append[_conversation.split(',')]      