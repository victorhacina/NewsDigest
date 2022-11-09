import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment():
    print("executing sentiment")
    text = """Președinta Comisiei Europene, Ursula von der Leyen, anunță că va efectua 
o vizită în Republica Moldova la mijlocul săptămânii viitoare.
 Într-o postare pe contul său de Twitter, Von der Leyen a declarat că se lucrează la un sprijin 
suplimentar pentru Republica Moldova pentru atenuarea crizei energetice."""

    lines = text.split(".")
    print(lines)
    for sentence in lines:
        sid = SentimentIntensityAnalyzer()
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

    words: list[str] = nltk.word_tokenize(text)
    fd = nltk.FreqDist(words)
    print(fd.most_common(10))
  