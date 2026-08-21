fruits = ["Banana", "Apple", "Mango"]
fruits.append("Guava")
fruits.remove("Apple")
fruits.sort()
for fruit in fruits:
    print(fruit)

squares = [x*x for x in range(10)]
print(squares)

evens = [x for x in range(20) if x%2==0]
print(evens)

#Focus: indexing, slicing, and the core mutation methods until they're automatic. 
# Problems: (1) Given a list of 10 numbers, print every 2nd element using slicing. 
num = [1,40,65,70,80,90,34,55,88,78]
print(num[1:10:2])

# (2) Reverse a list without using .reverse() or [::-1] — use a loop. 
for i in range(9,-1,-1):
    print(num[i])
# (3) Given two lists, merge them, remove duplicates, and sort — try both with a loop and with set(). 
l1 = [1,40,65,70,80,90,34,55,88,78]
l2 = [2,1,65,79,87,55]

merged_list = l1+l2

merged_list.sort()
final_list = []

for num in merged_list:
    if num in final_list:
        pass
    else:
        final_list.append(num)
    
print(final_list)

l1 = [1,40,65,70,80,90,34,55,88,78]
l2 = [2,1,65,79,87,55]

merged_list = l1+l2
final_list = set(merged_list)
final_list = sorted(final_list)
print(final_list)

# (4) Write a function that takes a list and returns a new list with each element doubled, using a loop,
#  then rewrite it as a one-line list comprehension. 
def list_comp(lst):
    new_list = []
    for num in lst:
       new_list.append(num * 2)
    return new_list

print(list_comp([2,3,4,6,7]))


# (5) Find the second-largest number in a list without using sort() or max() twice. 
def second_large(lst):
    largest = second = float('-inf')  
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

lst = [1,40,65,70,80,90,34,55,88,90,78]
print(second_large(lst))


# (6) Given a list of strings, return only the ones longer than 4 characters, using a list comprehension with a 
# condition.

def str_check(lst):
    final_lst = []
    for word in lst:
        if len(word) > 4:
            final_lst.append(word)

    return final_lst

lst = ["Ashwini","Pravin","Mira","Viju"]
print(str_check(lst))

# Basics & slicing
# Given nums = [12, 45, 3, 67, 21, 9, 88, 34], print the list in reverse using slicing 
# (not a loop this time — find the slice syntax for it).

nums = [12, 45, 3, 67, 21, 9, 88, 34]
print(nums[::-1])

# Given the same list, split it into two halves and print both 
# (don't hardcode the midpoint — calculate it using len()).
l1 = nums[:len(nums)//2]
print(l1)

l2 = nums[len(nums)//2:]
print(l2)

# Write a function rotate_left(lst, n) that rotates a list left by n positions. 
# E.g., rotate_left([1,2,3,4,5], 2) → [3,4,5,1,2]. 
# (Hint: slicing again — two slices concatenated.)

def rotate_left(lst, n):
    final_list= lst[n:]+ lst[:n]   
    return final_list

print(rotate_left([1,2,3,4,5,7,8,9], 3))


# Searching & counting
# 4. Write a function that finds all indices where a target value appears in a list (a value can repeat). 
# E.g., find_indices([1,2,3,2,4,2], 2) → [1, 3, 5].

def find_indices(lst, n):
    indices = []
    for i in range(len(lst)):
        if lst[i] == n:
            indices.append(i)

    return indices

print(find_indices([1,2,3,2,4,2], 2))


# 5. Given a list of numbers, count how many are positive, negative, and zero — return the three counts.

def num_count(lst):
    positive = 0
    negative = 0
    zero = 0
    for i in lst:
        if i == 0:
            zero += 1
        elif i % 2== 0:
            positive+=1
        else:
            negative += 1
    return(f"There are {zero} numbers are zero, {positive} are positive and {negative} are negative")

print(num_count([1,2,3,2,4,2, 3, 8,7,9,0,7,0]))
        

# 6. Write a function most_frequent(lst) that returns the most frequently occurring element in a list. 
# E.g., [1,2,2,3,2,4] → 2. (Hint: you already know a pattern for counting occurrences from the word-frequency exercise — 
# reuse that idea here.)

def most_frequent(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    best_num = None
    best_count = 0
    for num,count in frequency.items():
        if count > best_count:
            best_count = count
            best_num = num

    return best_num

print(most_frequent([1,2,3,2,4,2, 3, 8,7,9,0,7,0,3,3,4,4,4,4,4]))


# Transforming
# 7. Given a list of numbers, return a new list where each element is the running 
# total up to that point. E.g., [1,2,3,4] → [1,3,6,10] (1, 1+2, 1+2+3, 1+2+3+4).
# 8. Given a list of mixed positive/negative numbers, separate them into two lists — 
# positives and negatives — using one loop (not two separate filters).
# 9. Flatten a nested list. E.g., [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6]. Try it with a loop first.
# Challenge — combines everything
# 10. You're given a list of exam scores: scores = [55, 72, 88, 45, 91, 67, 39, 82, 100, 58]. 
# Without using sorted() or max()/min(): find the highest score, the lowest score, and the average — all in a single loop through the list (track running values as you go, like you did for second-largest).
# Work through these at your own pace — paste code as you go, in batches if you like, and I'll review. 
# #6, #9, and #10 are the ones worth spending real time on since they combine multiple things you've learned so far.