import nltk
from nltk import pos_tag



# POS tag pattern extraction
def pattern(text):
    patt = []
    sentence = nltk.word_tokenize(text)
    sent = pos_tag(sentence)
    force_tags = {'declare': 'VB', 'define': 'VB','write': 'VB', 'list': 'VB' , 'creating': 'NN', 'stand': 'VB', 'oriented': 'NN',
                  'overriding': 'NN', 'object': 'NN', 'generate': 'VB', 'check': 'VB', 'following': 'VB','name': 'VB','provide': 'VB',
                  'compare': 'VB','contrast': 'VB','suppose': 'VB','use': 'VB','select': 'VB','state': 'VB','java': 'NN','correct': 'VB',
                  'assign': 'VB','add': 'VB','print': 'VB','implement': 'VB','output': 'VB','arrange': 'VB','modify': 'VB'}
    new_tagged_words = [(word, force_tags.get(word, tag)) for word, tag in sent]
    for i in new_tagged_words:
        patt.append('<'+i[1]+'>')
    patter = ''.join(patt)
    return patter

# preprocessed input
q = "compare contrast array vector used java"
print("POS tag Pattern")
print(pattern(q))