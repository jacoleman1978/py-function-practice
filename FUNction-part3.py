# name_args Accepts any number of named arguments and prints them as 'key: value', one at a time
print("\n******name_args******")

def name_args(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")

name_args(a = "a", b = "b", nope = "huh?")

# all_true Returns True if all elements in an iterable are true
print("\n******all_true******")

def all_true(iterable):
    return all(iterable)

print(all_true([True, True, True, True]))
print(all_true([True, False, True, True]))
print(all_true([False, False, False]))

# one_true Returns True if one of the elements is true
print("\n******one_true******")

def one_true(iterable):
    return any(iterable)

print(one_true([True, True, True, True]))
print(one_true([True, False, True, True]))
print(one_true([False, False, False]))

# recursive_factorial uses recursion to find the factorial of an integer
print("\n******recursive_factorial******")

def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

print(recursive_factorial(3))
print(recursive_factorial(4))
print(recursive_factorial(5))

# recursive_deduplicate Recursively removes all adjacent duplicate letters from a string
print("\n******recursive_deduplicate******")

def recursive_deduplicate(string, prevOutput = ''):
    if string == '':
        return prevOutput
    else:
        prevOutput += string[0]
        if string[0] == string[1]:
            return recursive_deduplicate(string[2:], prevOutput)
        else:
            return recursive_deduplicate(string[1:], prevOutput)

test_string = 'AABBCCDD'
print(f"input: {test_string} \noutput: {recursive_deduplicate(test_string)}")

test_string = 'AaBbCCDD Worldd'
print(f"input: {test_string} \noutput: {recursive_deduplicate(test_string)}")

# recursive_reverse Recursively reverse a string
print("\n******recursive_reverse******")

def recursive_reverse(string, prevOutput = ""):
    length = len(string)
    if string == '':
        return prevOutput
    else:
        prevOutput += string[length - 1]
        return recursive_reverse(string[:length - 1], prevOutput)

test_string = 'AABBCCDD'
print(f"input: {test_string} \noutput: {recursive_reverse(test_string)}")

test_string = 'AaBbCCDD Worldd'
print(f"input: {test_string} \noutput: {recursive_reverse(test_string)}")