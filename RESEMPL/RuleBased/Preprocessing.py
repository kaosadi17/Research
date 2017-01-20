from nltk.stem import WordNetLemmatizer
import nltk
from nltk import pos_tag
import string, re, math
WORD = re.compile(r'\w+')
from nltk.tokenize import RegexpTokenizer


#tokenization
def tokenization(text):
    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    tokens = tokenizer.tokenize(text)
    return tokens

#punctuation removal
def removepunc(text):
    asking = "".join(l for l in text if l not in string.punctuation)
    return asking

#stopword removal
def stopwordRemoval(text):
    cachedStopWords = ["a","above","after","again","all","am","an","and","any","are","as","before","below","be",
                       "between","but","by","do","does","did","for","has","had","in","it","most","no","not","of","on","only","other","over","out",
                       "that","then","to","up","is"]
    text = text.lower()
    text1 = ' '.join([word for word in text.split() if word not in cachedStopWords])
    return text1

#lemmatization
def lemmatization(text):
    wnl = WordNetLemmatizer()
    lemm = []
    for word in text.split():
      lemm.append(wnl.lemmatize(word))
    lemm_sentence = ' '.join([i for i in lemm])
    return lemm_sentence


q = "Compare and contrast arrays and vectors used in Java?"
l = q.lower()
print("Case coverting : ")
print(l)
tok = tokenization(l)
print("Tokenizing : ")
print(tok)
punc = removepunc(l)
print("Punctuation Removing: ")
print(punc)
stop = stopwordRemoval(punc)
print("Stop word Removing: ")
print(stop)
lemm = lemmatization(stop)
print("Lemmatization: ")
print(lemm)





