import googletrans
from googletrans import Translator
from pprint import pprint


translator = Translator()
word = input("Give a word and it is translated to English and saved to list of translated words")
print(word)
print(googletrans.LANGUAGES)

try:
    result = translator.translate('Mikä on nimesi', src='fi')
except AttributeError:
    result = translator.translate('Mikä on nimesi', src='fi')



