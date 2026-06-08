class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def backtrack(val, path):
            if val == len(graph) - 1:
                result.append(path[:])
                return

            for x in graph[val]:
                path.append(x)
                backtrack(x, path)
                path.pop()
        backtrack(0, [0])

        return result