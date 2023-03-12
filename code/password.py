from googletrans import Translator
translator = Translator()
try:
    output = translator.translate('my name is simi.', dest='hi')
    print(output.text)
except AttributeError as e:
    print(f"Translation failed: {e}")
