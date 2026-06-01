'''Given a word and a text, return the count of the occurrences of anagrams of the word in the text.

For example, anagrams of "for" are "for", "orf", "ofr", "fro", "rof", etc.

Example:

Input:
forxxorfxdofr
for

Output:
3

Explanation:
Anagrams of the word "for" — "for", "orf", and "ofr" — appear in the text, so the count is 3.
'''

from collections import Counter

sentence = input()
word = input()

length = len(word)
result = 0

cnt = Counter(word)
window = Counter(sentence[:length])

if window == cnt:
    result += 1

for r in range(length, len(sentence)):
    window[sentence[r]] += 1

    left_char = sentence[r - length]
    window[left_char] -= 1

    if window[left_char] == 0:
        del window[left_char]

    if window == cnt:
        result += 1

print(result)