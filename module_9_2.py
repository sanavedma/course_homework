first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) > 5]
print(first_result)

second_result = [(s_1, s_2) for s_1 in first_strings for s_2 in second_strings if len(s_1) == len(s_2)]
print(second_result)

third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}
print(third_result)