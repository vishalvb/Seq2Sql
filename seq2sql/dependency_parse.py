from stanfordcorenlp import StanfordCoreNLP
from nltk import word_tokenize

nlp = StanfordCoreNLP('http://corenlp.run', port=80)
print(nlp.dependency_parse("What is the current series where the new series began in June 2011"))
postags = nlp.dependency_parse("What is the current series where the new series began in June 2011")

colums = ['State/territory', 'Text/background colour', 'Format', 'Current slogan', 'Current series', 'Notes']

nouns = ['NN','NNS','NNP','NNPS']
n = []
# for i in postags:
#     print('postag',i[0],'next',i[1])
question = 'what is the fuel propulsion where the fleet series (quantity) is 310-329 (20)?'
colums = ['Order Year', 'Manufacturer', 'Model', 'Fleet Series (Quantity)', 'Powertrain (Engine/Transmission)', 'Fuel Propulsion']
print(question.lower())

for col in colums:
    print(col.lower())
    print(question.lower().find(col.lower()))

print('postag',nlp.pos_tag(question))
#tokenize
c = 'Text/background colour'
print('c',c.split(sep='/'))