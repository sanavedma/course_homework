calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_len = len(string)
    str_upper = string.upper()
    str_lower = string.lower()
    info = (str_len, str_upper, str_lower)
    return tuple(info)


def is_contains(string, list_to_search):
    count_calls()
    if string.lower() in (item.lower() for item in list_to_search):
        return True
    else:
        return False

print(string_info('Urban'))
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)