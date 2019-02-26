import gensim, logging, smart_open, os

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = [['first', 'sentence'], ['second', 'sentence']]
model = gensim .models.Word2Vec(sentences, min_count=1)

filenames=['./data/f1.txt', './data/f2.txt'] 

for i,fname in enumerate(filenames):
    with smart_open.smart_open(fname, 'w') as fout: 
        for line in sentences[i]:
            fout.write(line + '\n')

class MySentences:
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in smart_open.smart_open(os.path.join(self.dirname, fname), 'r'):
                yield line.split()

sentences = MySentences('./data/')
print(list(sentences))

model = gensim.models.Word2Vec(sentences, min_count=1)
print(model)
print(model.wv.vocab)



