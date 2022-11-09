import boto3
from botocore.config import Config

def translate_text(txt,lang_source,lang_target):
    print("executing translate ")
    #client = boto3.client('translate')
    session = boto3.session.Session
    client = session.client(self, "translate")

    response = client.translate_text(
        Text=txt,
        SourceLanguageCode=lang_source,
        TargetLanguageCode=lang_target)

    result= response.get("TranslatedText")
    print(result)
