# from russtress import Accent
import transliterate

from russian_text_stresser.text_stresser import RussianTextStresser
try:
    from russtress import Accent
except ImportError:
    pass
def test_russtress():
    accent = Accent()
    text = "Проставь, пожалуйста, ударения"
    accented_text = accent.put_stress(text)
    print(accented_text)


TEST_TEXT = """
22 октября 2020 разработчики из Сбера объявили о создании русскоязычного аналога GPT-3. Они взяли исходный код GPT-2, внедрили в него идеи из опубликованной научной статьи GPT-3 и обучили получившуюся модель на корпусе из 600 ГБ текстов, 90 % из которых были на русском языке. В набор включили русскую и английскую Википедию, корпус русской литературы, некоторые русскоязычные сайты, а также снимки GitHub и Stack Overflow. Модель, которую они назвали ruGPT-3 Large, содержит 760 млн параметров[30]. В дальнейшем разработчиками были выложены версии модели на 1.3 млрд параметров (ruGPT-3 XL) и на 13 млрд параметров (ruGPT-3 13B).
"""

text = "У нашей девочки не было старой обуви на красных от холода ножках, не было старых перчаток на синих от холода ручках, и она ничего ни у кого не просила белыми от холода губами."

if __name__ == "__main__":
    # accentor = Accentor()
    print(transliterate.translit("хорошо́", reversed=True))
    print(transliterate.translit("Эта река уже чем я ожидал.", reversed=True))
    print(transliterate.translit("часа", reversed=True))

    

    #quit()

    text_stresser = RussianTextStresser()

    stressed_text = text_stresser.stress_text(TEST_TEXT)

    with open("stressed_text_test.txt", "w", encoding="utf-8") as f:
        f.write(stressed_text)

    print(stressed_text)
    quit()
    # Transliterate text to latin
    latin_text = transliterate.translit(TEST_TEXT, reversed=True)
    print(latin_text)
    # Stress text
    stressed_text = text_stresser.stress_text(TEST_TEXT)
    latin_stressed_text = transliterate.translit(stressed_text, reversed=True)
    print(latin_stressed_text)
