class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set([0])

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(rooms)==len(visited)

        '''
        visited = [0]  
        mark = [False]*len(rooms)

        while visited:
            ele = visited.pop(0)
            
            if mark[ele]:      # already visited, skip
                continue
                
            mark[ele] = True

            for i in rooms[ele]:
                if not mark[i]:   # add only if not visited
                    visited.append(i)

        return all(mark)


        #usings bfs
        visited = set([0])
        queue = deque([0])

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited)==len(rooms)


        
        # fails as you need to consider future rooms, which have keys to access all the rooms

        for i in range(len(rooms)):
            if i not in visited:
                return False
            for j in range(len(rooms[i])):
                visited.append(rooms[i][j])
        return True'''

        