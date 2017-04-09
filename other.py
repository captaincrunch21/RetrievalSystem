import pickle
import tf_idf
import xml.etree.ElementTree as ET
import operator
# from nltk.stem.snowball import SnowballStemmer
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
wordbank = pickle.load(open('word_bank.pkl','rb'))
model = tf_idf.model()
query = open('.\\rt\queries.txt','r').read()

root = ET.fromstring(query)
for queries in root.findall('top'):
    num = queries.find('num').text
    title = queries.find('title').text
    desc = queries.find('desc').text
    words = model.tokenizer(title+desc)
    score = {}
    for word in words:
        if word in wordbank:
            for document in wordbank[word]:
                if document[0] in score:
                    score[document[0]]+=document[1]
                else:
                    score[document[0]]=document[1]
    sorted_score = sorted(score.items(),key=operator.itemgetter(1),reverse=True)
    print(sorted_score)
    break



