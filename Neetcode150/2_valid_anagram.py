# sorting - time n log n + m log m : s n+m
def isAnagram1(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s.lower()) == sorted(t.lower())

# hash map - t n+m s 1
def isAnagram2(s: str, t: str) -> bool:
    if len(s)!= len(t):
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = countS.get(s[i], 0) +1
        countT[t[i]] = countT.get(t[i], 0) + 1

    return countS == countT

print(isAnagram2())

#hash table - tc m * n , sc  1
def isAnagram3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = [0] * 26
    
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] +=1
        count[ord(t[i])- ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
    
    return True
    
