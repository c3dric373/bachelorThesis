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
#print(list(sentences))
test_data_dir = '{}'.format(os.sep).join([gensim.__path__[0], 'test', 'test_data']) + os.sep
lee_train_file = test_data_dir + 'lee_background.cor' 


class MyText:
    def __init__(self, file):
        self.file = file

    def __iter__(self): 
        for line in open(self.file):
            yield line.lower().split()

sentences = MyText(lee_train_file)
model = gensim.models.Word2Vec(sentences, min_count=1)
model.evaluate_word_pairs(test_data_dir + 'wordsim353.tsv')


###################
#Testing our model with text8
###################


input_data = os.path.join(os.getcwd(), './data/text8')
print(input_data)
sentences = MyText(input_data)
newModel = gensim.models.Word2Vec(sentences)
print(newModel)
