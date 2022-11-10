import threading
from parse import parse_stiri
from translate import translate_text
from nlp import sentiment
print("executing main ")

lista = parse_stiri()
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

print("finish main")
