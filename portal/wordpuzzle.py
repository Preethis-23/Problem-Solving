m = int(input())
n = int(input())

arr = [list(input().strip()) for _ in range(m)]

visited = [[0]*n for _ in range(m)] 

num = int(input())
lst = [input().strip() for _ in range(num)]


def backtrack(r, c, word, ind):
    if r<0 or c<0 or r>=m or c>=n:
        return False
    if visited[r][c]==1:
        return False
    if arr[r][c]!=word[ind]:
        return False
    if len(word)-1==ind:
        return True
    visited[r][c] = 1
    result = backtrack(r, c+1, word, ind+1) or backtrack(r+1, c, word, ind+1)
    visited[r][c] = 0
    return result
    
    
for word in lst:
    flag = False
    for i in range(m):
        for j in range(n):
            if word[0]==arr[i][j]:
                if backtrack(i,j, word, 0):
                    flag = True
                    break
        if flag:
            break
    print(word,":","true" if flag else "false")

