first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(s_1) - len(s_2) for s_1, s_2 in zip(first, second) if len(s_1) != len(s_2))
print(list(first_result))

second_result = (len(first[s]) == len(second[s]) for s in range(min(len(first), len(second))))
print(list(second_result))