
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
train = sys.argv[1]
test = sys.argv[2]
number = []
con = []
content = []
topic = []
sentiment = []
a = ''
b = ''
remove = ['#','@','_', '$','%']
file = open(train,'r',encoding = 'UTF-8')
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
file.close()

    
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
clf = tree.DecisionTreeClassifier(criterion='entropy',random_state=0,min_samples_leaf=20)
model = clf.fit(X_train, Y_train)
#print(model.predict(test1))
number_t= []
con_t = []
content_t = []
topic_t = []
sentiment_t = []
a_t = ''
b_t = ''
file_test = open(test,'r',encoding = 'UTF-8')
for i in file_test:
    i = i.split('\t')
    number_t.append(i[0])
    con_t.append(i[1])
    topic_t.append(i[2])
    sentiment_t.append(i[3])
    
for j in con_t:
     new_t = []
     j = j.split()
     for k in j:
         if re.match("https://.*",k):
             continue
         c_t = [i for i in k if i.isalpha() or i.isdigit() or i in remove]
         b_t = ''.join(c_t)
         new_t.append(b_t)
     content_t.append(' '.join(new_t))
     
bag_of_words_t = count.fit_transform(content_t)
X =bag_of_words_t.toarray()
predicted_y = model.predict(X)
for i in range(len(predicted_y)):
    print(f'{number_t[i]} {predicted_y[i]}')

file_test.close()
   



        
   


        
   

   



        
   


        
   

        
   




   



        
   


        
   

   



        
   


        
   

        
   
   



        
   

   

        
   
        
   

       
    

   



        
   

   

        
   