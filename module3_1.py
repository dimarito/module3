call = 0


def count_call():
    global call
    call += 1


def string_info(string):
    count_call()

    info = [len(string), string.upper(), string.lower()]
    return tuple(info)


def is_contains(string, list_to_search):
    count_call()
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(call)
