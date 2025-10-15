"""
| Action                 | Works Automatically | Needs `global` | Best Practice            |
| ---------------------- | ------------------- | -------------- | ------------------------ |
| Read global variable   | ✅ Yes               | ❌ No           | Fine                     |
| Modify global variable | ❌ No                | ✅ Yes          | Avoid — pass as argument |
"""


# Print all elements of a list in reverse order using a loop (without using reversed() or slicing).
alph = ['a','b','c','d','e']
print(alph[1:3])
print(list(reversed(alph)))    #print(reversed(alph)) -> <list_reverseiterator object at 0x0000015052D56380>
print(max(alph))

dup = []
for i in range(len(alph)):
    # dup.append(i)
    print(i)
    dup.append(alph[-i-1])
print(dup)

dict = {}
for i in range(len(alph)):
    dict[alph[i]] = i

print(dict)


#Given a list of names, print only those starting with the letter 'A'
names = ['anirudh', 'cat', 'Avishkar', 'zebra']
valid = []
for name in names:
    if name[0].lower() == 'a':
        valid.append(name)

print(valid)

words = ["apple", "banana", "kiwi", "grapes", "mango"]
print([(len(words[i])) for i in range(len(words))])

num = [4,5,5,2,5,2,7,8,8,9]
max_num = max(num)
num.remove(max_num)
print(max(num))
num2 = sorted(num, reverse=True)
print(num2)
print(set(num2))
print(sorted(set(num2), reverse=True)[1])

#without dropping
numbers = [12, 45, 2, 41, 31, 10, 45, 22]
second_largest = 0
for i in numbers:
    if (i > second_largest) and (i != max(numbers)):
        second_largest = i
print(second_largest)

numbs = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]  # slicing creates a NEW list
print(reversed_list)
print(numbs)  # original list is unchanged

#reversing in place
nums2 = [10, 20, 30, 40, 50]
for i in range(len(nums2)//2):
    numx = nums2[i]
    nums2[i] = nums2[-i-1]
    nums2[-i-1] = numx
print(nums2)

numbers = [10, 20, 30, 40, 50]
n = len(numbers)
for i in range(n // 2):
    numbers[i], numbers[n - 1 - i] = numbers[n - 1 - i], numbers[i]
print(numbers)

# Flatten a nested list (e.g., [[1,2],[3,4,5],[6]] → [1,2,3,4,5,6]) using loops only.
# list = [[1,2],[3,4,5],[6]] 
# flattened = []
# for elements in list:
#     for i in elements:
#         flattened.append(i)
# print(flattened)

# Find all pairs of numbers in a list that sum to a given value.
numbers = [2, 4, 3, 5, 7, 8, 9]
target_sum = 10
empty_list = []
for i in range(len(numbers)):   # i-> 0 to 6
    for j in range(i+1, len(numbers)):   # if i=0 j=1 
        empty_list.append([numbers[i],numbers[j]])
print(empty_list)

print([i for i in empty_list if sum(i) == target_sum])

#OR
for i in range(len(numbers)):   # i-> 0 to 6
    for j in range(i+1, len(numbers)):   # if i=0 j=1 
        if numbers[i] + numbers[j] == target_sum:
            print(f"{numbers[i]}, {numbers[j]}")



#itertools
import itertools

numbers = [2, 4, 3, 5, 7, 8, 9]
target_sum = 10

for a, b in itertools.combinations(numbers, 2):  # all unique 2-element pairs
    print(a,b)
    if a + b == target_sum:
        print((a, b))

for com_with_rep in itertools.combinations_with_replacement(numbers,2):
    print(com_with_rep)

import itertools

nums = [1, 2, 3]
for p in itertools.permutations(nums):
    print(p)

# product(iter1, iter2, ...)	Cartesian product
# count(start, step)	Infinite counter
# cycle(iterable)	Loops forever through iterable
# repeat(item, n)	Repeats the same item n times

#Write a program to find the frequency of each element in a list using loops only (no Counter).
num3 = [2, 3, 5, 3, 7, 2, 2, 5, 8]
print(num3.count(3))
set3 = set(num3)
set_list3 = list(set3)
freq_dict = {}
for i in set_list3:
    count = 0
    for j in num3:
        if j == i:
            count += 1
    freq_dict[i] = f"{count} times" 
print(freq_dict)

    