"""
Create a matrix correctly.
Rotate a list without slicing.
Reverse a list in-place.
Remove duplicates while preserving order.
Explain why [[0]*n]*m is wrong.
Write a small function that demonstrates shallow copying.
"""
from typing import List

## creating matrix
def create_matrix(row,col):
    matrix = [[0]*col for _ in range(row)]
    print(matrix)

def reverse_list(arr):
    left,right = 0, len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

def rotate_list(arr):
    temp = arr[0]
    i=1
    for i in range(len(arr)):
        arr[i-1] = arr[i]

    arr[-1] = temp

def remove_dup(arr):
    unique = set()
    result = []
    for i in range(len(arr)):
        if arr[i] not in unique:
            unique.add(arr[i])
            result.append(arr[i])

# the first list is refrence of same list i.e. no new list object is created

def shallow_copy():
    data = [1,2,3,[4,8]]
    new_data = data.copy()

    new_data[3][0] = 8
    print(new_data)
    print(data)

def move_zeroes(arr: List[int]):
    left, right = 0, len(arr)
    while left < right:
        if arr[left] == 0:
            arr[left],arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        left += 1

        print(arr)

def is_palindrome(s):
    left, right = 0,len(s)-1
    while left < right:
        if not s[left].isalpha():
            left +=1
        if not s[right].isalpha():
            right -= 1
        if not (s[left].lower() == s[right].lower()):
            print("false")
            break
        left += 1
        right -= 1
    print(True)

def comprehense():
    nums = [1,2,3,4,5,6,7,8,9,10]

    #evens
    evens = [x for x in nums if x%2==0]
    odd_sq = [x*x for x in nums if x%2 != 0 ]
    num_str = [str(x) for x in nums]

    # enumerate
    names = ["Alice","Bob","Charlie","David"]

    for index, value in enumerate(names):
        print(f"{index} -> {value}")

    # zip
    scores = [95,80,91]
    score_list = list(zip(names,scores))
    print(score_list)

comprehense()

def word_frequency(sentence):
    freq_count = {}
    words = list(sentence.split())
    for word in words:
        freq_count[word] = freq_count.get(word,0) + 1
    print(freq_count)

# for a=b the output will be same list since for small size array, int and other value pythons maintains refrence and 
# same list object is refrenced for a and b

def second_largest(arr):
    first = arr[0]
    second = 0
    for i in range(1,len(arr)):
        if first < arr[i]:
            second = first
            first = arr[i]

    print(second)

def prop_arr(arr):
    length = 0
    max = float("-inf")
    min = float("inf")
    for num in arr:
        length += 1
        if max < num:
            max = num
        if min > num:
            min = num