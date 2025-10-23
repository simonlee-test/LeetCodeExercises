def scoreOfString(s: str) -> int:
    score : int = 0
    for i in range(len(s) -1):
        score += abs(ord(s[i])-ord(s[i+1]))
    return score

print(scoreOfString("hello"))