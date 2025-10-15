"""
| Action                 | Works Automatically | Needs `global` | Best Practice            |
| ---------------------- | ------------------- | -------------- | ------------------------ |
| Read global variable   | ✅ Yes               | ❌ No           | Fine                     |
| Modify global variable | ❌ No                | ✅ Yes          | Avoid — pass as argument |
"""



































































































































































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


    