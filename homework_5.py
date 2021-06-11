# 1
def odd_nums(max_value):
    n = 1
    while n <= max_value:
        yield n
        n += 2

odd_to_15 = odd_nums(15)
print(odd_to_15)

#3
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
def gen_of_people():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield (None, klasses[i])
            i += 1
            j += 1
            break
        else:
            yield (tutors[j], klasses[i])
            i += 1
            j += 1
for gen in gen_of_people():
    print(gen)

#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(result)

#5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])
