# Errors, Exceptions and saving JSON Data

# with open('samplefile.txt') as f:
#     f.read()
# # FileNotFoundError: [Errno 2] No such file or directory: 'samplefile.txt'

# a_dict = {'key':'value'}
# value = a_dict['key2']
# # KeyError: 'key2'

# my_list = [1,2,6,8]
# my_list[6]
# # IndexError: list index out of range

# text = 'abc'
# text + 5
# # TypeError: can only concatenate str (not "int") to str

# Murphy's Law - Anything that could get wrong, will get wrong some time or the other
"""
try:
    file = open('a_file.txt')
    a_dict = {'key':'value'}
    value = a_dict['key']
    print(value)
except FileNotFoundError:                                         # You should not use a bare except, because it will then ignore all type of errors
    file = open('a_file.txt', 'w')
    file.write('something')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')

# If the except block also fails, then code will crash
# But if the finally block exist, it will still run, but the program will still crash afterward (because of the unhandled error in the except).
    
else:    # when the try block is executed without any error
    content = file.read()
    print(content)           # Had try block not executed, except will get executed, and hence, this else will not get executed
finally:
    file.close()
    print('file was closed')
    raise KeyError('This is a key error I customized')
    
"""
    
height = float(input('Height: '))
weight = int(input('weight: '))

if height > 3:
    raise ValueError('Human height should be less than 3m')

bmi = weight/height**2
print(bmi)

