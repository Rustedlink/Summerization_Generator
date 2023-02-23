#Natural Language Toolkit
import nltk

#important modules and librarys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from collections import defaultdict


def summarize(user_Input, percent=0.3):
    # to create sentences and words
    sentences = sent_tokenize(user_Input)
    words = word_tokenize(user_Input.lower())

    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = []
    word: object
    for word in words:
        if word not in stop_words:
            words.append(word)

    # Calculate word frequency
    freq = defaultdict(int)
    for word in words:
        assert isinstance(word, object)
        freq[word] += 1

    # Calculate sentence scores based on word frequency
    scores = defaultdict(int)
    for j, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                scores[j] += freq[word]

    # Calculate the number of sentences to retain based on percentage
    num_sentences = max(1, int(len(sentences) * percent))

    # Sort sentences by score and return the top n
    top_n = sorted(scores.items(), key=lambda item: item[1], reverse=True)[:num_sentences]
    top_n_indices = [index for index, score in top_n]
    summary = ' '.join([sentences[i] for i in sorted(top_n_indices)])
    return summary


# Get user input for summarize and the percentage
text = input("What would you like to be summarized: ")
percent = float(input("Enter the percentage of text you would like to be summarized (example 0.3 for 30%): "))

# Summarize the text and print the result
summary = summarize(text, percent)
print(summary)
