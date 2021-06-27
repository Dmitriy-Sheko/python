#1
english_to_rusian = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(english):
    return english_to_rusian.get(english)
print(num_translate('one'))
print(num_translate('eight'))
print(num_translate('something'))

#3
def thesaurus(*names):
    output = dict()
    for name in names:
        output.setdefault(name[0], [])
        output[name[0]].append(name)
    return output
print(thesaurus("Игорь", "Маруся", "Алексей", "Виктор"))

#5
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(number):
    joke_list = []
    for i in range(number):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list
print(get_jokes(1))
print(get_jokes(2))
