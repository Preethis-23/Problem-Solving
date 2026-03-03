from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        que = deque([beginWord])
        visited = set([beginWord])
        parents = defaultdict(list)
        found = False

        while que and not found:
            level_visited = set()

            for _ in range(len(que)):
                word = que.popleft()

                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in word_set and new_word not in visited:
                            if new_word == endWord:
                                found = True

                            if new_word not in level_visited:
                                que.append(new_word)
                                level_visited.add(new_word)

                            parents[new_word].append(word)

            visited.update(level_visited)

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return

            for p in parents[word]:
                dfs(p, path + [p])

        if found:
            dfs(endWord, [endWord])

        return res