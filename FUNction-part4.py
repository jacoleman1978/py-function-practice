import math

# max_num: Find the maximum of three numbers
'''
Input: 3 numbers: num1, num2, num3
Output: no returned value, prints maximum of three given numbers
'''
print("\n******max_num******")
def max_num(num1, num2, num3):
    max = num1
    if num2 > max:
        max = num2
    elif num3 > max:
        max = num2
    
    print(f"input: {num1}, {num2}, {num3} \n{max} is the maximum\n")

max_num(12, 18, 4)
max_num(0, 12, -87)

# mult_list: multiply all the numbers in a list
'''
Input: list of numbers
Output: no returned value, prints product of all numbers in the list
'''
print("\n******mult_list******")
def mult_list(num_list):
    product = 1
    for num in num_list:
        product *= num
    
    print(f"input: {num_list} \nThe product of those numbers is {product}\n")

num_list = [2, 2, 2, 2]
mult_list(num_list)

num_list = [2, 2, 0, 2]
mult_list(num_list)

num_list = [2, -2, 2, 2]
mult_list(num_list)

# rev_string: reverse a string
'''
Input: a string
Output: returns reversed string
'''
print("\n******rev_string******")
def rev_string(string, prevOutput = ""):
    length = len(string)
    if string == '':
        return prevOutput
    else:
        prevOutput += string[length - 1]
        return rev_string(string[:length - 1], prevOutput)

test_string = 'AABBCCDD'
print(f"input: {test_string} \noutput: {rev_string(test_string)}")

test_string = 'AaBbCCDD Worldd'
print(f"input: {test_string} \noutput: {rev_string(test_string)}")

# fib: calculates the nth Fibonacci number
'''
Input: an integer
Output: returns the value of nth Fibonacci number
'''
print("\n******fib******")
def fib(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = 12
print(f"Fibonacci value at position {n}: {fib(n)}")

# num_within: determine if a number falls within a given range
'''
Input: num_to_check, range_start, range_end (inclusive)
Output: returns boolean
'''
print("\n******num_within******")
def num_within(num_to_check, range_start, range_end):
    if num_to_check >= range_start and num_to_check <= range_end:
        return True
    else:
        return False

def test_num_within(input_as_list):
    '''
    Input: input_as_list is a list of lists, each containing num_to_check, range_start, range_end (inclusive)
    Output: no return value, prints inputs and outputs
    '''
    for input in input_as_list:
        is_within = num_within(input[0], input[1], input[2])
        print(f"Input: check if {input[0]} is inclusively between {input[1]} and {input[2]} \nOutput: {is_within}\n")

input_as_list = [[3, 2, 4], [3, 1, 3], [10, 2, 5]]
test_num_within(input_as_list)

# pascal: prints out the first n rows of Pascal's triangle
'''
Input: integer n for how many rows to print
Output: no return value, prints each line
'''
print("\n******pascal******")
def pascal(n):
    current_row = [1]

    if n > 1:
        for row_num in range(1, n + 1):
            previous_row = current_row[:]
            current_row = [1]
            for row_position in range(1, row_num):
                if row_position == row_num - 1:
                    current_row.append(1)
                else:
                    position_value = previous_row[row_position] + previous_row[row_position - 1]
                    current_row.append(position_value)
            row_string = ''
            for num in current_row:
                row_string += " " + str(num)

            print(row_string)

pascal(6)