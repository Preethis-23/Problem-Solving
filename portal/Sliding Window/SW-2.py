'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input:
ABAB
2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
AABABBA
1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

from collections import defaultdict

ch = input()
k = int(input())

default = defaultdict(int)

l = 0
result = 0
freq = 0

for r in range(len(ch)):
    default[ch[r]] += 1

    freq = max(freq, default[ch[r]])

    while (r - l + 1) - freq > k:
        default[ch[l]] -= 1
        l += 1

    result = max(result, (r - l + 1))

print(result)