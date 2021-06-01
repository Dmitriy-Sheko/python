#Homework1
#1
duration = int(input('Введите время в секундах: '))
f_day = (60 * 60 * 24)
f_hour = (60 * 60)
days = duration // f_day
hours = (duration - days * f_day) // f_hour
minutes = (duration - days * f_day - hours * f_hour) // 60
seconds = duration - days * f_day - hours * f_hour - minutes * 60
print(f'{days} дни {hours} час {minutes} мин {seconds} cек')

#2
list = []
for number in range(1, 1001, 2):
    list.append(number ** 3)
sum = 0
for number in list:
    check_sum = 0
    for check_number in str(number):
        check_sum += int(check_number)
    if check_sum % 7 == 0:
        sum += number
print(sum)
sum = 0
for number in list:
    number += 17
    check_sum = 0
    for check_number in str(number):
        check_sum += int(check_number)
    if check_sum % 7 == 0:
        sum += number
print(sum)

#3
percent = int(input('Введите количество процентов: '))
if percent == 1:
    word = 'процент'
elif percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)
