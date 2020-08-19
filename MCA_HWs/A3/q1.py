import keras
from keras.layers import Dense 
import os
import numpy as np
import nltk
import pandas as pd
import random
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


words_list = nltk.corpus.abc.words()
stopwords = nltk.corpus.stopwords.words()
words_without_stopwords = [word for word in words_list if not word in stopwords]

ind = random.randint(0,492603)
f_words = words_without_stopwords[ind:ind+10000]

one_hot_en = []
for i in range(10000):
    temp = np.zeros(10000)
    temp[i] = 1
    one_hot_en.append(temp)
one_hot_en[0].shape

def create_trainiable_tuples(window_size,one_hot_en):
    x = []
    y = []
    for i in range(10000):
        tail = max(0,i-window_size)
        head = min(10000,i+window_size+1)
        for j in range(tail,head):
            if j!=i:
                x.append(one_hot_en[i])
                y.append(one_hot_en[j])
    return x,y            
x,y = create_trainiable_tuples(1,one_hot_en)
xt = np.array(x)
yt = np.array(y)

model = keras.models.Sequential()
model.add(Dense(300,input_shape = (10000,)))
model.add(Dense(10000,activation = 'softmax'))

model.compile(loss = 'binary_crossentropy',optimizer = 'adam')
model.fit(xt,yt,verbose = 1)

words = []
x_test = []
r = np.arange(9999)
for i in range(20):
    ind = random.choice(r)
    words.append(f_words[ind])
    x_test.append(one_hot_en[ind])
    np.delete(r,ind)


words = np.array(words)
x_test = np.array(x_test)
#ind = random.randint(0,9980)
#words = f_words[ind:ind+20]
#x_test = np.array(one_hot_en[ind:ind+20])
y_pred = model.predict(x_test,verbose = 1)

#Reducing dimensions
pca = PCA (n_components = 2)
x_y_plt = pca.fit_transform(y_pred)

x_y_plt = x_y_plt*np.power(10,6)

df = pd.DataFrame(x_y_plt, columns = ['x', 'y'])
df['word'] = words
df = df[['word', 'x', 'y']]
print(df)

fig, ax = plt.subplots()

for word, x1, x2 in zip(df['word'], df['x'], df['y']):
    ax.annotate(word, (x1,x2 ))
    
k = 1.0
a = np.amin(x_y_plt, axis=0)[0] - k
b = np.amax(x_y_plt, axis=0)[0] + k
c = np.amin(x_y_plt, axis=0)[1] - k
d = np.amax(x_y_plt, axis=0)[1] + k
 
plt.xlim(a,b)
plt.ylim(c,d)
plt.rcParams["figure.figsize"] = (10,10)

plt.show()