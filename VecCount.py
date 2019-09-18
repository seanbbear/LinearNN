from gensim.models import word2vec
from gensim import models
import logging

from udicOpenData.stopwords import *

with open('3000.txt','r',encoding='utf-8') as f:
    word = f.readlines()
    for i in range(len(word)):
        if "1" in word[i][0]:
            print(word[i])
    
        
    
    