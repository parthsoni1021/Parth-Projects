"""
| Action                 | Works Automatically | Needs `global` | Best Practice            |
| ---------------------- | ------------------- | -------------- | ------------------------ |
| Read global variable   | ✅ Yes               | ❌ No           | Fine                     |
| Modify global variable | ❌ No                | ✅ Yes          | Avoid — pass as argument |
"""

# Section1: Lists and Loops

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


# Bubble -sort algorithm
arr = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)):  # i -> 0 to 7
    for j in range(i+1, len(arr)):    # j -> 1 to 7 (if i is 0)
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

#Remove duplicates without using set()
dup_lists = [1,4,6,8,2,4,1,7,8,5]
set_dup = set(dup_lists)
print(set_dup)
print(list(set_dup))

for i in dup_lists:
    if dup_lists.count(i) > 1:  #without using count function, loop 'j' from 'i+1 to len, and compare. If same, drop j
        dup_lists.remove(i)
print(dup_lists)

# Merge two sorted lists into one sorted list (without using sort() or sorted()).
sort1 = [7,9,12,13]
sort2 = [2,4,6,8,10,19,20]
new_sorted = []
i = 0
j = 0
while i < len(sort1) and j < len(sort2):
    if sort1[i] < sort2[j]:
        new_sorted.append(sort1[i])
        i += 1
    elif sort1[i] == sort2[j]:
        new_sorted.append(sort1[i])
        new_sorted.append(sort2[j])
    else:
        new_sorted.append(sort2[j])
        j += 1 

new_sorted.extend(sort1[i:])      #append v/s extend
new_sorted.extend(sort2[j:])

print(new_sorted)


# Pattern
patternlist = [1,2,3,4,5,6,7,8]
i = 0
pattern = []
while i < len(patternlist):
    pattern.append(patternlist[i])
    print(*pattern)                  #notice the *
    i+=1

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
i = 0
j = 0
zip_list = []
while i < len(list1) and j < len(list2):
    zip_list.append((list1[i],list2[j]))
    i += 1
    j += 1
print(zip_list)

print(list(zip('abcdefg', range(3), range(4))))


#Section 2 :Functions, String manupulations, Dictionaries, Sets and File handling
