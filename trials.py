"""Python functions for JavaScript Trials 1."""

group = ['item1', 'item2', 'item3']
nums_all = [1, 2, 4, 5, 7, 8,]
def output_all_items(items):
    pass  
    for item in items:
        # print(item)
        return items

output_all_items(group)

def get_all_evens(nums):
    pass  
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    # print(even_nums)
    return even_nums

get_all_evens([7, 8, 10, 1, 2, 2])

def get_odd_indices(items):
    pass  # TODO: replace this line with your code
    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(items[i])    
    # print(result)
    return result

get_odd_indices([1, 'hello', True, 500])

def print_as_numbered_list(items):
    pass  
    i = 1
    for item in items:
        # print(f'{i}. {item}')
        i += 1
print_as_numbered_list([1, 'hello', True])


def get_range(start, stop):
    pass  
    nums = []
    i = start
    for i in range(stop):
        nums.append(i)
        # print(nums)

get_range(0, 5)

def censor_vowels(word):
    pass  
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    return ''.join(chars)

censor_vowels('hello world')

def snake_to_camel(string):
    pass  
    camel_case = []
    word = string.split("_")
    print(word)
        # camel_case.append(upper(word))
    
snake_to_camel('hello_world')


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
