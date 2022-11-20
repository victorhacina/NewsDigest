import boto3
import threading
import re

client = boto3.client("translate")

def translate_text(txt,lang_source,lang_target,lista):
    print(f"executing translate { threading.current_thread()}")
   
    response = client.translate_text(
        Text=txt,
        SourceLanguageCode=lang_source,
        TargetLanguageCode=lang_target)

    result= response.get("TranslatedText")
    result_clean= re.sub(r'[^\w\s.,\-\'\"]', '', result)
    lista.append(result_clean)
    return



