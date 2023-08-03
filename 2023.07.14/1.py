num_1 = float (input('Введите число 1: '))
num_2 = float (input('Введите число 2: '))
num_3 = float (input('Введите число 3: '))

sum_of_num = num_1 if num_1 > 0 else 0
sum_of_num += num_2 if num_2 > 0 else 0
sum_of_num += num_3 if num_3 > 0 else 0

print ('Сумма положительных чисел: ',sum_of_num)

#Введите число 1: 3
#Введите число 2: 4
#Введите число 3: -6
#Сумма положительных чисел:  7.0
