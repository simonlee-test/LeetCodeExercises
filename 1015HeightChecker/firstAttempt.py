from typing import List

def heightChecker(heights: List[int]) -> int:
    notOrdered = 0
    expected = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != expected [i]:
            notOrdered +=1
    return notOrdered

heights= [1,1,4,2,1,3]


print(heightChecker(heights))