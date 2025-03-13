def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

values_list = [5, False, 'University']
values_dict = {'a': True, 'b': [1, 2, 3], 'c': 'Привет, Мир!'}
values_list_2 = ['String', 47]

print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)