# ПЕРЕИМЕНОВАТЬ: переменным требуется давать имена по смыслу, так чтобы код можно было удобнее и быстрее читать — имя t очень мало говорит о том, какое значение ассоциировано с данной переменной — вместо него стоило назвать переменную minutes
t = int(input('Введите время в минутах'))
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (лишний пробел)
print(f'{t} мин - это {t // 60} час  {t % 60} минут')


# Введите время в минутах 150
# 150 мин - это 2 час  30 минут


# \n не является же обязательным в данном случае? Просто с новой строки?
# КОММЕНТАРИЙ: '\n' — это и есть символ конца строки, без него "с новой строки" не получится
# ОТВЕТИТЬ: в данной задаче он не используется явным образом, но откуда-то берётся аж два раза: откуда?


# ИТОГ: хорошо, немного доработать — 2/3


# КОММЕНТАРИЙ: следите за пробелами:
#  в коде — потому что 1) в Python это имеет значение для отступов 2) оформленный в одном стиле код намного удобнее читать, а для этого всем требуется следовать одному стилю (потому и существует PEP 8)
#  в выводе — потому что строки, которые вы будете генерировать в коде, чаще всего будут предназначены для другого кода, а не для человека
