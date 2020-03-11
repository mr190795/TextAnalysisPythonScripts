import nltk

all_answers = ("""""")

st_words = [',', 'I', 'if', 'my', 'the', '1)', '2)', '3)', 'are', 'is', '.', 'to', '''I'd''', '-', 'by', 'for', 'and', '''doesn't''', 'then',
            'go', 'from', 'there', 'will', 'like', 'at', 'did', 'weren', "don't", 'few', 'it', 'his', 'is', 'so', 'now', "wouldn't", "shan't",
            'she', "shouldn't", "won't", 'which', 'will', 'nor', 'out', "should've", 'you', 'themselves', 'because', 'theirs', 'too', 'on', 'me',
            'under', 'up', 'during', "you've", 'those', "it's", 'are', 'no', 'before', 'against', 'couldn', 've', 'ourselves', 'in', 'won', "didn't",
            'such', "haven't", "mustn't", 'once', 'who', 'an', 'most', 'same', 'if', 'he', 'does', 'my', 'further', 'here', "hasn't", 'we', 'these',
            'have', 'hers', 'any', 'not', 'as', 'above', 'should', 'down', 'after', 'being', 'having', 'wasn', 'y', 'your', 'its', 'then', 'am', 'has',
            'haven', 'why', 'were', 'was', 'for', 'while', 'of', 're', 'isn', 'himself', 't', 'hadn', 'itself', 'about', 'between', 'aren', "needn't",
            "hadn't", 'where', "aren't", 'off', "that'll", 'i', 'they', 'own', 'doing', 'but', "weren't", 'other', 'what', 'yourselves', 'do', 'only',
            'below', 'her', 'yours', 'herself', 'd', 'the', 'all', 'their', 'doesn', 'myself', 'didn', 'a', 'our', 'don', "you'd", 'by', 'again', 'into',
            'through', 'had', 'll', "doesn't", 'can', 'just', 'been', 'than', 'ma', 'mightn', "she's", 'be', 'very', 'him', 'some', 'hasn', 'how', 'needn',
            'm', "isn't", "you're", 'to', "mightn't", 'wouldn', 'at', 'and', 'shan', 'each', "you'll", 'this', 'when', 'both', 'ain', 'mustn', 'or', 'shouldn',
            'more', 'that', 'yourself', 'until', 'with', 'them', 'from', 's', 'ours', "couldn't", 'over', 'there', "wasn't", 'o', 'whom', 'If', 'set', 'look', 'would',
            'For', 'see', 'first', 'need', 'This', ')', '(', "'d", 'make', 'The', 'also', 'want', 'one', 'whether', 'either', 'start',
            'We', 'looking', 'may', "'nt", 'could', 'using', 'use', 'might', 'data', 'able', 'going', "'", 'us', "n't"]

from nltk.tokenize import sent_tokenize
token_sent = sent_tokenize(all_answers)

from nltk.tokenize import word_tokenize
token_word = word_tokenize(all_answers)

filter_word = [ ]
for w in token_word:
    if w not in st_words:
        filter_word.append(w)

from nltk.probability import FreqDist
fdist = FreqDist(filter_word)

import matplotlib.pyplot as plt
fdist.plot(50,cumulative = False)
plt.show()



