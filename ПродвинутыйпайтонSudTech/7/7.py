# python test_1.py раз 2

from argparse import ArgumentParser # импортируем модуль argparse и его класс ArgumentParser, который позволяет создавать парсер аргументов командной строки

parser = ArgumentParser(description='Принимаем строку с параметрами') # создаем объект парсера
parser.add_argument('first_parameter', type=str, default='раз', help='Первый параметр') # добавляем аргумент first_parameter, который будет строкой и имеет значение по умолчанию 'раз'
parser.add_argument('second_parameter', type=str, default='два', help='Второй параметр') # добавляем аргумент second_parameter, который будет строкой и имеет значение по умолчанию 'два'

args = parser.parse_args() # парсим аргументы командной строки и сохраняем их в

#from sys import argv # импортируем модуль sys и его функцию argv, которая позволяет получать аргументы командной строки

#p_1 , p_2, p_3 = argv # распаковываем аргументы командной строки в переменные p_1 и p_2
#print(p_1, p_2, p_3) # выводим значения переменных p_1 и p_2
print(args.first_parameter, args.second_parameter) # выводим значения аргументов first_parameter и second_parameter, которые были переданы через командную строку