#!/usr/local/bin/python3
import os
import xml.etree.ElementTree as ET
from nltk.stem.snowball import SnowballStemmer
import string
from collections import Counter as count
import math
import dill

class model(object):
    def __init__(self,location=''):
        self.location = location
        self.stop = [w.strip() for w in open('stop.txt').readlines()]
        self.stemmer = SnowballStemmer("english")
        self.word_bank = {}
        self.total_len = 0


    def tokenizer(self,infor):
        new = []
        for word in infor.split(' '):
            word = word.translate(None, string.punctuation)
            if word not in self.stop and word:
                t = self.stemmer.stem(word)
                new.append(t)
        return new
    def modelMaker(self):
        for dirName, subdirList, fileList in os.walk(self.location):
            for file in fileList:
                self.total_len+=1
                print (self.total_len)
                try:
                    t = open(dirName + "\\" + file)
                    t_read = t.read()

                    try:
                        root = ET.fromstring(t_read)
                    except:
                        continue
                    doc_no = root.find('DOCNO').text
                    title = root.find('TITLE').text
                    text = root.find('TEXT').text
                    result = self.tokenizer(title + text)
                    for word in result:
                        if word in self.word_bank:
                            self.word_bank[word].append(doc_no)
                        else:
                            self.word_bank[word] = []
                            self.word_bank[word].append(doc_no)
                except:
                    continue
        self.tf_idf()



    def tf_idf(self):
        for word in self.word_bank:
            print(word)
            temp = self.word_bank[word]
            t = count(temp)
            te = t.keys()
            tv = t.values()
            w = []
            for name in range(len(te)):
                tr = tv[name] * math.log10(self.total_len / len(te))
                # print (te[name], tr)
                w.append([te[name], tr])
            self.word_bank[word]=w

    def makePickle(self):
        dill.dump(self.word_bank,open('word_bank.pkl','wb'))

    def doshit(self):
        pass