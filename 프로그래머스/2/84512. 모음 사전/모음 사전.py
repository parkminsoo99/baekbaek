alphaList = ["A","E","I","O","U"]

import copy
resultCount = 0
found = False
def dfs(count, target, temp):
    global resultCount,found
    if found:
        return
    if temp == target:
        found = True
        return 
    if count == 5:
        return
    for i in range(5):
        resultCount += 1
        dfs(count+1, target, temp + alphaList[i])
        if found:
            return resultCount
            
    return resultCount
def solution(word):
    answer = dfs(0, word, "")
    return answer