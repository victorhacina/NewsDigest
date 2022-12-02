import threading
from parse import parse_stiri,parse_jurnal,parse_publica,parse_realitatea,parse_tv8,parse_pointmd,parse_protv
from translate import translate_text
from nlp import sentiment,frequency
import json


print("executing main ")

lista = parse_stiri()+ parse_jurnal()+ parse_publica()+ parse_tv8()+ parse_realitatea()+ parse_pointmd()+ parse_protv()

print(lista)

threads = []
results = []

for el in lista:
    if(el["titlu"] in ["pointmd"] ): 
        thread = threading.Thread(target=translate_text, args=(el['brief'], "ru", "en", results))
    else:
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
for el in results: all = all + el
  

most_common = frequency(all)
print(most_common)

result = {"news": scores, "words": most_common}

file_scores = open("result.txt", "w", encoding = "utf-8")
file_scores.write(json.dumps(result))
file_scores.close()

print("finish main")
