import threading
from parse import parse_stiri
from translate import translate_text

print("executing main ")

lista = parse_stiri()
print(lista)

threads = []
results = []

for el in lista:
    thread = threading.Thread(target=translate_text, args=(el['brief'], "ro", "en"))
    threads.append(thread)
    thread.start()

for element in threads: 
    element.join()

print(results)
print("finish main")

#TODO: de mutat in fisier separat
#sentiment()

