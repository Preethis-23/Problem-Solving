"""Question:
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input:
target = 7
nums = [2,3,1,2,4,3]

Output:
2

Example 2:
Input:
target = 4
nums = [1,4,4]

Output:
1
"""

target = int(input())
arr = list(map(int, input().split()))

l = 0
curr_sum = 0
ans = float("inf")

for r in range(len(arr)):
    curr_sum += arr[r]

    while curr_sum >= target:
        ans = min(ans, r - l + 1)
        curr_sum -= arr[l]
        l += 1

print(0 if ans == float("inf") else ans)