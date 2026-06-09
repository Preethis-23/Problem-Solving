class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        ans = float("inf")
        session = []

        def backtrack(ind):
            nonlocal ans
            if ind == len(tasks):
                ans = min(ans, len(session))
                return
            if len(session) >= ans:
                return
            for x in range(len(session)):
                if session[x] + tasks[ind] <= sessionTime:
                    session[x] += tasks[ind]
                    backtrack(ind + 1)
                    session[x] -= tasks[ind]
            session.append(tasks[ind])
            backtrack(ind + 1)
            session.pop()
        backtrack(0)
        return ans

