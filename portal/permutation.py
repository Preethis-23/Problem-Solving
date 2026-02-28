s = input().strip()

s = sorted(s)       
used = [False] * len(s)
path = []
r = []
def backtrack():
    if len(path) == len(s):
        r.append(path.copy())
        return
    
    for i in range(len(s)):
        if used[i]:
            continue
        
        used[i] = True
        path.append(s[i])
        
        backtrack()
        
        path.pop()
        used[i] = False

backtrack()
print(len(r))
for i in r:
    print("".join(i))