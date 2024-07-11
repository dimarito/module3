# Задача "Распаковка"

# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(2, 'новая строчка1', False)
print_params(b='новая строчка2', c=False)
print_params(a=3, c=True)

# 2. Распаковка параметров
value_list = [5, 'новая строчка3', False]
value_dict = {'a': 12, 'b': 'новая строчка4', 'c': True}

print_params(*value_list)
print_params(**value_dict)

# 3. Распаковка + отдельные параметры
values_list_2 = [100, 'новая строчка5']
print_params(*values_list_2, 42)