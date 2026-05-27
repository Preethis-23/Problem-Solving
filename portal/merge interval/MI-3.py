'''Given two strings s1 and s2, return True if s2 contains any permutation of s1, otherwise return False.

Example:
Input:
ab
eidbaooo

Output:
True

Explanation:
"ba" is present in s2, which is a permutation of "ab".'''


from collections import Counter

s1 = input()
s2 = input()

def perm(s1, s2):

    n = len(s1)

    if n > len(s2):
        return False

    c1 = Counter(s1)
    c2 = Counter()

    for i in range(len(s2)):

        c2[s2[i]] += 1

        # maintain fixed window size
        if i >= n:

            left = s2[i - n]

            c2[left] -= 1

            if c2[left] == 0:
                del c2[left]

        # compare frequency maps
        if c2 == c1:
            return True

    return False

print(perm(s1, s2))