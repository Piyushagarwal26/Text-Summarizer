import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

def summarize(text, n):
    stop_words = set(stopwords.words('english'))
    word_freq = {}
    for word in word_tokenize(text.lower()):
        if word not in stop_words:
            if word not in word_freq.keys():
                word_freq[word] = 1
            else:
                word_freq[word] += 1
    
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/max_freq)
        
    sent_list = sent_tokenize(text)
    sent_score = {}
    for sent in sent_list:
        for word in word_tokenize(sent.lower()):
            if word in word_freq.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sent_score.keys():
                        sent_score[sent] = word_freq[word]
                    else:
                        sent_score[sent] += word_freq[word]
                        
    summary_sents = nlargest(n, sent_score, key=sent_score.get)
    summary = ' '.join(summary_sents)
    return summary

text = input('Enter text to summarize: ')
summary = summarize(text, 3)
print(summary)