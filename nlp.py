import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.sentiment.vader import SentimentIntensityAnalyzer



def sentiment(text):
    print("executing sentiment")
      
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    return ss["compound"]
    # for k in sorted(ss):
    #     print('{0}: {1}, '.format(k, ss[k]), end='')
    # print("\n")


def frequency(txt):
    words: list[str] = nltk.word_tokenize(txt)
    words_tagged = nltk.pos_tag(words)
    words_relevant = []
    for (word, tag) in words_tagged:
        if tag[0:2] in ["RB", "NN", "JJ"]: 
            words_relevant.append(word)
    fd = nltk.FreqDist(words_relevant)
    return fd.most_common(10)

