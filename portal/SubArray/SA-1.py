"""992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example:

Input:
nums = [1,2,1,2,3]
k = 2

Output:
7

Explanation:

The 7 good subarrays are:

[1,2]
[2,1]
[1,2]
[2,3]
[1,2,1]
[2,1,2]
[1,2,1,2]

--------------------------------------------------

Approach:

exactly(k) = atMost(k) - atMost(k-1)

For this example:

exactly(2) = atMost(2) - atMost(1)

--------------------------------------------------

Calculate atMost(2)

r = 0
window = [1]
valid subarrays ending at 0:
[1]

add 1
count = 1

--------------------------------------------------

r = 1
window = [1,2]
valid subarrays ending at 1:
[1,2]
[2]

add 2
count = 3

--------------------------------------------------

r = 2
window = [1,2,1]
valid subarrays ending at 2:
[1,2,1]
[2,1]
[1]

add 3
count = 6

--------------------------------------------------

r = 3
window = [1,2,1,2]
valid subarrays ending at 3:
[1,2,1,2]
[2,1,2]
[1,2]
[2]

add 4
count = 10

--------------------------------------------------

r = 4
window = [1,2,1,2,3]

distinct = 3

shrink:

[2,1,2,3]
still 3 distinct

[1,2,3]
still 3 distinct

[2,3]
now 2 distinct

valid subarrays ending at 4:
[2,3]
[3]

add 2
count = 12

--------------------------------------------------

atMost(2) = 12

--------------------------------------------------

Calculate atMost(1)

Valid subarrays:

[1]
[2]
[1]
[2]
[3]

count = 5

atMost(1) = 5

--------------------------------------------------

Final Answer

exactly(2)
=
atMost(2) - atMost(1)
=
12 - 5
=
7"""


from collections import Counter

def atmost(nums, k):
    l = 0
    cnt = 0
    freq = Counter()

    for r in range(len(nums)):
        freq[nums[r]] += 1

        while len(freq) > k:
            freq[nums[l]] -= 1

            if freq[nums[l]] == 0:
                del freq[nums[l]]

            l += 1

        cnt += r - l + 1

    return cnt