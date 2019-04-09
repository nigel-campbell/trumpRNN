import nltk
from nltk.util import ngrams
from collections import defaultdict
import random
import argparse

parser = argparse.ArgumentParser(description='Ngram Model')
parser.add_argument('--data', type=str, default='../../data/full_dataset.txt',
                    help='location of data corpus')
parser.add_argument('--n', type=int, default=3,
                    help='random seed')

args = parser.parse_args()

fname = args.data

data = []
f = open(fname, 'rb')
data = [line for line in f]
f.close()

"""
Trains ngram model
"""
def train(n, data):
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for tweet in data:
        for words in list(ngrams(tweet.split(), n, pad_right=True, pad_left=True)):
            prefix, suffix = words[:n-1], words[n-1]
            model[prefix][suffix] += 1
    # Generates probabilities
    for prefix in model:
        total_count = float(sum(model[prefix].values()))
        if total_count > 0:
            for suffix in model[prefix]:
                model[prefix][suffix] /= total_count
    return model

def generate(model, n, seed=None, debug=True):
    text = [None] * (n - 1)
    if seed:
        text = seed
    sentence_finished = False
    while not sentence_finished:
        r = random.random()
        #r = random.randint(0,1e6) * 1e-10 
        accumulator = 0.0
        prefix_key = tuple(text[-(n-1):]) 
        for word in model[prefix_key].keys():
            accumulator += model[prefix_key][word]
            
            if accumulator >= r:
                text += [word]
                break
                
        if text[-n:] == [None]*(n):
            sentence_finished = True
        
        if debug and len(' '.join(filter(None, text))) > 240:  # Hacky. TODO Fix
            sentence_finished = True
        
    l = len(text)
    return text[n:l-n]

n = args.n
print("Training {}-gram".format(n))
model = train(n, data)
for i in range(3):
    text = generate(model, n, debug=True)
    text = ' '.join(filter(None, text))
    print('{}\n'.format(text))



model[None, None]
