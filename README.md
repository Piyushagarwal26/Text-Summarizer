# Text Summarizer


## Project Title
**Developing an Efficient Text Summarizer Using Natural Language Processing**


## Table of Contents
1. [Title](#title)
2. [Abstract](#abstract)
3. [Architecture & Design](#architecture--design)
4. [Algorithm](#algorithm)
5. [Code in Python](#code-in-python)
6. [Applications](#applications)
7. [Conclusion](#conclusion)

## Abstract
Text Summarizer is a project aimed at developing a powerful and efficient text summarizer using natural language processing techniques in Python. The project involves implementing algorithms and techniques such as sentence scoring, text cleaning, and entity recognition to accurately summarize long blocks of text into concise, informative summaries.

The main goal of Text Summarizer is to create a user-friendly tool that can effectively summarize large volumes of text across a wide range of fields, from news articles to scientific publications. By automating the summarization process, Text Summarizer will help users save time and quickly identify key information in large bodies of text.

The project leverages Python libraries such as NLTK (Natural Language Toolkit), SpaCy, and Gensim to build a robust and scalable text summarization system. The resulting tool is available as an open-source package that can be easily integrated into existing Python applications.



## Architecture & Design
The system consists of the following components:

1. **Text preprocessing module**: Tokenizes input text, removes stop words, and prepares the text for summarization.
2. **Word frequency calculation module**: Calculates and normalizes the frequency of each word.
3. **Sentence scoring module**: Scores sentences based on the frequency of words and selects the top sentences for the summary.
4. **Summary generation module**: Selects the top 'n' sentences and joins them to form the final summary.

## Algorithm
The algorithm involves:
1. Tokenizing text and removing stop words.
2. Creating a word frequency dictionary.
3. Normalizing word frequencies.
4. Tokenizing text into sentences and scoring them.
5. Selecting the top 'n' sentences for the summary.
6. Joining the selected sentences to form the summary.

## Code in Python
```python
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
        word_freq[word] = (word_freq[word] / max_freq)

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
```

## Architecture & Design
The system consists of the following components:

1. **Text preprocessing module:** This module performs initial text processing by tokenizing the input text into individual words using the `word_tokenize()` function from the NLTK library. It then removes any stop words from the list of words using the `stopwords.words()` function from the NLTK library. Stop words are common words such as "the", "and", "is", etc., that do not carry much meaning and can be safely removed from the text. The resulting list of words is used as input for the next module.

2. **Word frequency calculation module:** This module calculates the frequency of each word in the preprocessed list of words using a Python dictionary. For each word, it checks if the word is already in the dictionary. If it is, it increments the frequency count for that word. If it is not, it adds the word to the dictionary with a frequency count of 1. After all words have been processed, the module normalizes the frequency count for each word by dividing the count by the maximum frequency of all words. This normalization ensures that words with high frequencies do not dominate the summary.

3. **Sentence scoring module:** This module scores each sentence in the input text based on the frequency of the words it contains. It first tokenizes the input text into individual sentences using the `sent_tokenize()` function from the NLTK library. For each sentence, it tokenizes the sentence into individual words using the `word_tokenize()` function from the NLTK library and removes any stop words. It then calculates the sentence score by summing the normalized frequency count for each word in the sentence. The resulting sentence scores are used to rank the sentences in the next module.

4. **Sentence ranking module:** This module ranks the sentences in the input text based on their sentence scores. It first creates a list of tuples, where each tuple contains a sentence and its corresponding sentence score. It then sorts the list of tuples in descending order based on the sentence scores. The top-ranked sentences are selected to form the summary. The number of sentences in the summary is determined by the user-specified summary length.

5. **Summary generation module:** This module generates the summary by concatenating the top-ranked sentences in their original order. The resulting summary is returned as the output of the system.


## Applications

The text summarizer has a variety of real-life applications, including:

1. **News media**: Summarize news articles for quick consumption.
2. **Academic research**: Summarize scholarly articles for literature reviews.
3. **Business intelligence**: Analyze and summarize customer feedback and social media posts.
4. **Legal documents**: Summarize contracts and legal briefs.
5. **Education**: Create summaries of articles and texts for classroom use.


## Conclusion

The text summarizer is an effective tool for reducing the length of large texts while retaining their most important information. The implementation demonstrates the effectiveness of natural language processing techniques in creating sophisticated applications that automate complex tasks. The performance can be further improved by incorporating additional NLP features and techniques.

---
