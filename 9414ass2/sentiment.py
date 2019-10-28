# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:57:57 2019

@author: kyrie
"""

import numpy as np
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import PorterStemmer
import sys



#remove all the stopwords
def remove_stopwords(content):
    text = []
    english_stopwords = stopwords.words('english')
    st = PorterStemmer()
    for i in content:
        tag = (word_tokenize(i))
        tag_remove_stopwords = [i for i in tag if i not in english_stopwords]
        texts_stemmed = [st.stem(word) for word in tag_remove_stopwords]
        text.append(' '.join(texts_stemmed))
    return text

with open(sys.argv[1],'r',encoding = 'UTF-8') as file:
    number = []
    con = []
    content = []
    topic = []
    sentiment = []
    a = ''
    b = ''
    remove = ['#','@','_', '$','%']
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
         
with open(sys.argv[2],'r',encoding = 'UTF-8') as file:
    number_t = []
    con_t = []
    content_t = []
    topic_t = []
    sentiment_t = []
    at = ''
    bt = ''
    remove_t = ['#','@','_', '$','%']
    for i in file:
        i = i.split('\t')
        number_t.append(i[0])
        con_t.append(i[1])
        topic_t.append(i[2])
        sentiment_t.append(i[3])
    
    for j in con:
         new_t = []
         j = j.split()
         for k in j:
             if re.match("https://.*",k):
                 continue
             ct = [i for i in k if i.isalpha() or i.isdigit() or i in remove]
             bt = ''.join(c)
             new_t.append(b)
         content_t.append(' '.join(new_t))
         
content = remove_stopwords(content)    
content_t = remove_stopwords(content_t)
#print(content)
#print(sentiment)
# Create text
text_data = np.array(content)
text_data_t = np.array(content_t)
# Create bag of words
count = CountVectorizer(lowercase=False,max_features=400)
bag_of_words = count.fit_transform(text_data)
bag_of_words_t = count.fit_transform(text_data_t)
#print(count.get_feature_names())

# Create feature matrix
X = bag_of_words.toarray()
A= bag_of_words_t.toarray()
# Create target vector
Y = np.array(sentiment)
B = np.array(seniment_t)


X_train = X
Y_train = Y

X_test = A
Y_test = B

# Create new unseen test instances
#test1 = count.transform(['I like Italy, because Italy is beautiful']).toarray()


clf =  MultinomialNB()
model = clf.fit(X_train, Y_train)

#print(model.predict(test1))

for i in range(len(model.predict(X_test))):
    print(f'{number[i]} {model.predict(X_test)[i]}')
#model.predict(X_train)
    
'''
print('2',model.predict(X_test))
print('3',model.predict_proba(X_test))
print('4',accuracy_score(Y_test,model.predict(X_test)))
print('5',precision_score(Y_test,model.predict(X_test),average = None))
print('6',recall_score(Y_test,model.predict(X_test),average = None))
print('7',f1_score(Y_test, model.predict(X_test), average='micro'))
'''

   



        
   


        
   

   



        
   


        
   

        
   
   



        
   

   


