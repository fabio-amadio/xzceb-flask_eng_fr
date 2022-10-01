"""Translator module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path(os.path.dirname(os.path.abspath(__file__))+'/.env')
load_dotenv(dotenv_path=dotenv_path)

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translate a english text into french."""
    try:
        result = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    except ValueError:
        return None
    else:
        french_text = result["translations"][0]["translation"]
        return french_text

def french_to_english(french_text):
    """Translate a french text into english."""
    try:
        result = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    except ValueError:
        return None
    else:
        english_text = result["translations"][0]["translation"]
        return english_text
