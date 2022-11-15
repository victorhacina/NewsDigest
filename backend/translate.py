import boto3
from botocore.config import Config

client = boto3.client("translate")

def translate_text(txt,lang_source,lang_target,lista):
    print("executing translate ")
   
    response = client.translate_text(
        Text=txt,
        SourceLanguageCode=lang_source,
        TargetLanguageCode=lang_target)

    result= response.get("TranslatedText")
    lista.append(result)
    return
