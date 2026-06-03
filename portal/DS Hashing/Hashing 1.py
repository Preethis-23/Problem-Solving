# Question:
# Create a Hash table to store and display number of elements 'n' using Separate Chaining method.
# The first line of the input is the number of elements 'n'.
# The second line of the input is the insertion elements.
# Note: The size of hash table is equal to the number of elements 'n'.

'''
Input:
5
45 67 55 78 12

Hashing:
45 % 5 = 0
67 % 5 = 2
55 % 5 = 0
78 % 5 = 3
12 % 5 = 2

Hash Table:
index 0 : 45->55->
index 1 : No Hash Entry
index 2 : 67->12->
index 3 : 78->
index 4 : No Hash Entry'''

n = int(input())
lst = list(map(int, input().split()))

hashmap = [[] for _ in range(n)]

for i in lst:
    ind = i % n
    hashmap[ind].append(i)

for i in range(len(hashmap)):
    print("at index", i)

    if hashmap[i]:
        for x in hashmap[i]:
            print(x, end='->')
        print()
    else:
        print("No Hash Entry")