from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize
from nltk import wordpunct_tokenize
# from pycorenlp import StanfordCoreNLP
#
#
# nlp = StanfordCoreNLP('http://localhost:9000')


nlp = StanfordCoreNLP('http://corenlp.run', port=80)
print(nlp.pos_tag("What school did the player that has been in Toronto from 2012-present come from"))
postags = nlp.pos_tag("What school did the player that has been in Toronto from 2012-present come from")

colums = ['Player', 'No.', 'Nationality', 'Position', 'Years in Toronto', 'School/Club Team']

nouns = ['NN','NNS','NNP','NNPS','JJ','JJR','JJS']
n = {}
for i in range(len(postags)):
    if(postags[i][1] in nouns):
        print('word = ',postags[i][0])
        n[i] = (postags[i][0])

print('n=',n)
# if(n[3]+' '+n[4] in word_tokenize("What is the current series where the new series began in June 2011")):
#     print(n[3])

# if(n[3] in map(str.lower,colums)):
#     print('found')
probabalecolum = {}
for colum in colums:
    tokens = wordpunct_tokenize(colum)
    length = len(tokens)
    score= 0
    for i in range(length):
        if(tokens[i].lower() in n.values()):
            score += 1
    print('score',score,'length',length,'colum',colum)
    if(score > 0):
        probabalecolum[colum] = score;
    if(score == length):
        print('colum',colum)

print('probable',probabalecolum)
for col in probabalecolum:
    print()