#Homework_2
#1
print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 3))
print(type(15 ** 3))

#2
list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for element in list:
    if element.isdigit():
        new_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        new_list.extend(['"', f'{element[0]}{int(element[1:]):02}', '"'])
    else:
        new_list.append(element)
output = ' '.join(new_list)
print(output)

#4
incorrect_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in incorrect_list:
    print('Привет', position.split()[-1].title())

#5
prices = [17.3, 34.5, 26, 11, 21.44, 31.2, 7.15, 55.6, 707, 2]
for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')
prices = [17.3, 34.5, 26, 11, 21.44, 31.2, 7.15, 55.6, 707, 2]
print(id(prices))
prices.sort()
print(id(prices))
for price in prices:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп')
prices = [17.3, 34.5, 26, 11, 21.44, 31.2, 7.15, 55.6, 707, 2]
for price in sorted(prices)[::-1][:5]:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп')
print([f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][:5]])
