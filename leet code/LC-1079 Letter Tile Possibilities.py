class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        used = [False] * len(tiles)

        def backtrack(path):
            for i in range(len(tiles)):
                if used[i]:
                    continue
                # choose
                used[i] = True
                path.append(tiles[i])
                result.add("".join(path))
                # explore
                backtrack(path)
                # undo choice
                path.pop()
                used[i] = False
        backtrack([])
        return len(result)
