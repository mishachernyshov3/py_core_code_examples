# Create translation context manager.
LANGUAGE = 'en'

trans_dict = {
    'greeting': {
        'en': 'Hello. I am a bot that will help you to generate an image.',
        'uk': 'Привіт. Я бот, який допоможе вам згенерувати зображення.',
        'fr': 'Bonjour. Je suis un bot qui va vous aider à générer une image.',
    },
    'image_type': {
        'en': 'What the image type would you like to get?',
        'uk': 'Який тип зображення ви хотіли б отримати?',
        'fr': "Quel type d'image souhaitez-vous obtenir?",
    }
}


def translate(phrase):
    if translations := trans_dict.get(phrase):
        return translations[LANGUAGE]
    return None


class LanguageSwitcher:
    def __init__(self, lang_code):
        self.lang_code = lang_code
        self.__default_lang = None

    def __enter__(self):
        global LANGUAGE
        self.__default_lang = LANGUAGE
        LANGUAGE = self.lang_code
        return self

    def __exit__(self, *args):
        global LANGUAGE
        LANGUAGE = self.__default_lang


with LanguageSwitcher('uk'):
    print(translate('greeting'))
    with LanguageSwitcher('fr'):
        print(translate('image_type'))
    print(translate('image_type'))

print(translate('greeting'))
print(translate('image_type'))
