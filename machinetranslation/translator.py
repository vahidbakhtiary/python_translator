"""IBM Watson"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


URL = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/' \
      'instances/66982877-6908-4a41-a610-9ca943318ec4'
API_KEY = 'j-SoWvrojS940XWrFdSILs7D0N54G72x_-f5OdumUPua'

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url(URL)


def english_to_french(text1):
    """
    This function translate english to french
    """

    french_translation = language_translator.translate(text= text1 , model_id="en-fr").get_result()

    return french_translation.get("translations")[0].get("translation")


def french_to_english(text1):
    """
    This function translate french to english
    """

    english_translation = language_translator.translate(text= text1 , model_id="fr-en").get_result()

    return english_translation.get("translations")[0].get("translation")
