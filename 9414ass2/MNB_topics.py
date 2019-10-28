
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:01:43 2019

@author: kyrie
"""

import sys
import numpy as np
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn import tree
import re
train = 'dataset.tsv'
test = 'data.tsv'
number = []
con = []
content = []
topic = []
sentiment = []
a = ''
b = ''
remove = ['#','@','_', '$','%']
with open(train,'r',encoding = 'UTF-8',errors='ignore') as file:
    
    for i in file:
    
        i = i.split('\t')
        number.append(i[0])
        con.append(i[1])
        topic.append(i[2])
        sentiment.append(i[3])
    
    for j in con:
         new = []
         j = j.split()
         for k in j:
             if re.match("https://.*",k):
                 continue
             c = [i for i in k if i.isalpha() or i.isdigit() or i in remove]
             b = ''.join(c)
             new.append(b)
         content.append(' '.join(new))
         

    
#print(content)
#print(sentiment)
# Create text
text_data = np.array(content)
# Create bag of words
count = CountVectorizer(lowercase=False,max_features=200)
bag_of_words = count.fit_transform(text_data)
#print(count.get_feature_names())
# Create feature matrix
X = bag_of_words.toarray()
# Create target vector
Y = np.array(topic)
X_train = X
Y_train = Y
# Create new unseen test instances
#test1 = count.transform(['I like Italy, because Italy is beautiful']).toarray()
clf =  MultinomialNB()
model = clf.fit(X_train, Y_train)
#print(model.predict(test1))
number_t= []
con_t = []
content_t = []
topic_t = []
sentiment_t = []
a_t = ''
b_t = ''
file_test = open(test,'r',encoding = 'UTF-8',errors='ignore')
for i in file_test:
    i = i.split('\t')
    print(i)

   



        
   


        
   

   



        
   


        
   

        
   




   



        
   


        
   

   



        
   


        
   

        
   
   



        
   

   

        
   
        
   

       
    


   



        
   


        
   

   



        
   


        
   

        
   
   



        
   




        
   


        
   

   



        
   


        
   

        
   
   



        
   

   