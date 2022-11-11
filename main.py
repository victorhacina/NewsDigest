import threading
from parse import parse_stiri,parse_jurnal
from translate import translate_text
from nlp import sentiment,frequency
import re

print("executing main ")

lista = parse_stiri()+ parse_jurnal()

print(lista)

threads = []
results = []

for el in lista:
    thread = threading.Thread(target=translate_text, args=(el['brief'], "ro", "en", results))
    threads.append(thread)
    thread.start()

for element in threads: 
    element.join()

#print(results)



scores = []
for el in results:
   score = sentiment(el)
   scores.append({"sentence":el, "score":score})
print(scores)

all = ""
for el in results:
    all = all + el
  
all_filter = re.sub(r'[^a-zA-Z0-9\s]', '', all)

most_common = frequency(all_filter)
print(most_common)
    

print("finish main")
