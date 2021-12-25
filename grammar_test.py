# coding=utf-8
import spacy

from russian_dictionary import RussianDictionary

nlp = spacy.load('ru_core_news_sm')
#string = "Шарик улетел от Максима."
#string = "Он говорил о дворе"
#nlp.disable_pipes("ner")

yo_test1 = "Мое копье красивое."
yo_test2 = "Это песня о копье."
stress_test1 = "Твои слова ничего не значат."
stress_test2 = "Почему не стоит говорить (и писать) фразу «от слова совсем»"

test3 = "Больше всего на свете Джоэл хочет стать рифматистом."
test4 = "Девушка вбежала в гостиную и остановилась, не зная, как поступить дальше. В углу тикали напольные часы, освещенные луной. В широком панорамном окне виднелись очертания раскинувшегося города: здания поднимались на десять этажей и выше, между ними протянулись линии пружинной дороги. Джеймстаун, ее дом все шестнадцать лет жизни."
test5 = "Масляные капли, брызнув на расписную стену и дорогой ковер, заблестели в лунном свете."

test6 = "Если они умирали в бою, то попадали туда сразу же."
test7 = "Почему-то это не удалось."
test8 = "Он пробил деревянные стены насквозь и продолжил полет, его шлем скрежетал о камни."
test9 = "Далинар грозной тенью замер в дверном проеме."

doc = nlp(test9)
#spacy.displacy.serve(doc, style='dep')
rd = RussianDictionary()

for token in doc:
    print(token.text)
    print("#" + token.whitespace_ + "#")
    print(token.pos_)
    print(token.morph.to_dict())
    print(rd.get_stressed_word_and_set_yo(token.text, token.pos_, token.morph))