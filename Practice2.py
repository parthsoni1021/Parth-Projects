# # # Section 2 :Functions, String manupulations, Dictionaries, Sets and File handling

# # # Write a function is_prime(n) that checks whether a number is prime. Use it to find all primes in a list.
# # def isprime(n):
# #     for i in range(2,n):
# #         if n % i == 0:
# #             return False
# #     return True
# # list1 = [2,5,7,8,10,11,12,13]
# # print([isprime(i) for i in list1])

# # # Write a recursive function factorial(n) to compute factorial.
# # def factorial(n):
# #     if n in [0,1]:
# #         return 1
# #     else:
# #         return n * factorial(n-1)
    
# # print(factorial(5))

# # # Function reverse_string(s) that reverses a string without using slicing.
# # def rev_str(string):
# #     newstr = ""
# #     for i in range(len(string)-1,-1,-1): 
# #         newstr += string[i]
# #         print(i)
# #     return newstr

# # print('parth'[3])
# # print(rev_str("parth"))

# # # better solution
# # def rev_str2(string):
# #     for i in string:
# #         newstr = "" + i
# #     return newstr

# # # Function count_vowels_consonants(s) that returns a dictionary like {"vowels": 3, "consonants": 5}.
# # def count_vowels_consonants(word):
# #     dict_vowels_consonants = {
# #         "vowels": 0,
# #         "consonants": 0
# #     }
# #     vowels = list('aeiou')
# #     for i in word.lower():
# #         if i in vowels:
# #             dict_vowels_consonants["vowels"] += 1
# #         else:
# #             dict_vowels_consonants["consonants"] += 1
            
# #     return dict_vowels_consonants

# # print(count_vowels_consonants('ParthSoni'))

# # Write a function fibonacci(n) that returns the first n Fibonacci numbers as a list.
# # output = [0,1,1,2,3,5,8,13,21,34,55] n terms

# def fib(n):
#     a = 0
#     b = 1   
#     fib_list = [0,1]
#     while len(fib_list) < n:
#         fib_list.append(a+b)        
#         a,b = b, a+b
#     return fib_list

# print(fib(11))

# Function flatten_list(lst) to convert a nested list like [1, [2, 3], [4, [5,6]]] → [1,2,3,4,5,6].
def flatten_list(lst, flat_list = None):
    if flat_list == None:
        flat_list = []    
        
    for i in lst:
        if type(i) in (int, bool, float, str):
            flat_list.append(i)
        else:
            for j in i:
                if type(j) in (int, bool, float, str):
                    flat_list.append(j)
                else:
                    flatten_list(j, flat_list)
                               
    return flat_list
                
print(flatten_list([1, [2, 3], [4, [5,6]],[[1, [2, 3], [4, [5,6,7,8]]]]]))   # WOW MOMENT !! But here the flat_list is outside the function, which is problematic

# Simpler solution
def flat_the_list(lst):
    empty_lst = []
    for i in lst:
        if isinstance(i, list):
            empty_lst.extend(flat_the_list(i))
        else:
            empty_lst.append(i)
    return empty_lst

print(flat_the_list([1, [2, 3], [4, [5,6]],[[1, [2, 3], [4, [5,6,7,8]]]]]))

# Write a decorator to greet someone before and after using a function
def greet(fx):
    def wrapper(*args, **kwargs):
        print('Welcome')
        fx(*args, **kwargs)
        print('Thanks for using')
    return wrapper

@greet
def hello():
    print("Hello World")

hello()

# What python does is, hello() = greet(hello)()

@greet
def add(a,b):
    print(a+b)
    
add(1,3)

#  Logging decorator

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
    
@logging_decorator
def add(a,b):
    return a+b

print(add(2,6))

# Write a decorator timer to measure execution time of any function.
import time 
def measure_time(fx):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func = fx(*args, **kwargs)
        duration = round((time.time() - start_time),6)
        print(f"{fx.__name__} took {duration} seconds to execute.")
        return func
    return wrapper

@measure_time
def slow_function():
    time.sleep(1)
    return "Done"

slow_function()

# Function apply_func(lst, func) that applies a function func to every element of lst.
def apply_func(lst, func):
    result_list = []
    for i in lst:
        result_list.append(func(i))
    return result_list    

def square(x):
    return x*x

print(apply_func([1,3,5,7,9], square))

def gm(list):
    product = 1
    for i in list:
        product *= i
    result = product ** (1/len(list))
    return result
lst = [i for i in range(1,11)]
print("Geometric mean:",gm(lst))

def hm(list):
    res = 0
    for i in list:
        res += (1/i)
    result = (len(list)/res)
    return result
print("Harmonic mean:",hm(lst))

def am(list):
    return sum(list)/len(list)
print("Arithmetic mean:",am(lst), "\nHM penalises the lowest")









