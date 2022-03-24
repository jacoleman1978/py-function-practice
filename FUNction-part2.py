print("****arb_args****")

def arb_args(*args):
    for arg in args:
        print(arg)

arb_args(12, "hey", "peacock", "rainbow")

###########################################
print("\n****inner_func****")

def inner_func(num1, num2):
    def multiplyNums(num1, num2):
        return num1 * num2
    
    def plus12(num1):
        return num1 + 12
    
    sum = multiplyNums(num1, num2) + plus12(num1)

    print(sum)

inner_func(7, 4)

###########################################
print("\n****lunch_lady****")

def lunch_lady(student_name, preferred_meal = "Mystery Meat"):
    print(f"{student_name} really likes {preferred_meal}")

lunch_lady("Jamie", "Mushroom Swiss Burgers")

###########################################
print("\n****sum_n_product****")

def sum_n_product(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

print(sum_n_product(4, 7))

###########################################
print("\n****alias_arb_args****")

alias_arb_args = sum_n_product
print(sum_n_product(6, 3))

###########################################
print("\n****arb_mean****")

def arb_mean(*nums):
    sample_size = len(nums)
    sum = 0

    for num in nums:
        sum += num
    
    mean = sum / sample_size

    print(mean)

arb_mean(70, 80, 90, 100)

###########################################
print("\n****arb_longest_string****")

def arb_longest_string(*strings):
    max_length = 0
    max_string = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            max_string = string
    
    return max_string

print(arb_longest_string("dog", "cat", "sloth", "elephant", "turtle"))