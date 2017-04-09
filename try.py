import os
import xml.etree.ElementTree as ET
from nltk.stem.snowball import SnowballStemmer
import string
from collections import Counter as count
import math

stop = [w.strip() for w in open('stop.txt').readlines()]
stemmer = SnowballStemmer("english")

def tokenizer(infor):
    new = []
    for word in infor.split(' '):
        word = word.translate(None, string.punctuation)
        if word not in stop and word :

            t = stemmer.stem(word)
            new.append(t)

    return new
word_bank = {}
for dirName, subdirList, fileList in os.walk(".\\rt"):
    for file in fileList:
        t = open(dirName+"\\"+file)
        t_read = t.read()

        root = ET.fromstring(t_read)
        doc_no = root.find('DOCNO').text
        title = root.find('TITLE').text
        text = root.find('TEXT').text
        result = tokenizer(title+text)
        for word in result:
            if word in word_bank:
                word_bank[word].append(doc_no)
            else:
                word_bank[word]=[]
                word_bank[word].append(doc_no)
file = 0
for word in word_bank:
    temp = word_bank[word]
    t = count(temp)
    # print(t.keys(),t.values())
    file +=1
    te = t.keys()
    tv = t.values()
    w = []
    # print(te)
    for name in range(len(te)):

        tr =tv[name]*math.log10(4/len(te))
        print (te[name],tr)
        w.append([te[name],tr])
        # print (te[name],tv[name]*math.log10(4/len(te)))

    print('word completed')
    print("-----------------------")
    print(w)
    print("-------------------------")
    if file >1:
        break
