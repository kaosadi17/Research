import re, math
WORD = re.compile(r'\w+')
from collections import Counter

# read defined rules
def read_rules():
    with open("rules.txt") as textFile:
        rules = [line.split() for line in textFile]
    return rules

#text to vector conversion
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

#cosine similarity
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

#calculate cosine similarity
def cosine_method(ques_pat, patterns):
    cosine_sim = []
    back = []
    for pattern in patterns:
        for tagpat in pattern:
            s1 = text_to_vector(ques_pat)
            s2 = text_to_vector(tagpat)
            x = get_cosine(s1,s2)
            back.append(x)
        sumval = sum(back)
        cosine_sim.append(sumval)
        back = []
    #print(cosine_sim)
    return cosine_sim

def order_cos(semlist):
    array = []
    indexes =  sorted(range(len(semlist)), key=lambda k: semlist[k])
    new_indexes = list(reversed(indexes))
    taxonomy_cat = ["remember","understand","apply","analyze","evaluate","create"]
    for i in new_indexes:
        array.append(taxonomy_cat[i])
    print(array[0])

#pos tag pattern of question
pattern =  "<VB><VB><NN><NN><VBD><NN>"
rules = read_rules()
cosine_values = cosine_method(pattern,rules)
order_cos(cosine_values)
