original_number = int(input('Insira um número: '))
copy_number = original_number
reversed_number = 0
while original_number > 0:
    remainder = original_number % 10
    reversed_number = reversed_number * 10 + remainder
    original_number = original_number // 10
if copy_number == reversed_number:
    print(copy_number, 'é um número palíndromo')
else:
    print(copy_number, 'não é um número palíndromo')