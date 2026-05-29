from typing import List
from collections import defaultdict

#sorting - tc n log n sc n
def longestConsecutive( nums: List[int]) -> int:
    if not nums:
        return 0
    
    res = 0
    nums.sort()
    
    curr,streak = nums[0], 0
    
    i = 0
    
    while i < len(nums):
        if curr != nums[i]:
            curr = nums[i]
            streak=0
        while i < len(nums) and nums[i] == curr:
            i+=1
        
        streak +=1
        curr +=1
        res= max(res,streak)
    
    return res

#hash set - tc n, sc n
def longestConsecutive1(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0
    
    for num in numSet:
        if (num-1) not in numSet:
            length =1 
            while (num + length) in numSet:
                length+=1
            longest=max(length, longest)
    return longest


print(longestConsecutive1(nums=[2, 20, 4, 10, 3, 4, 5]))

#hash map - tc n, sc n
def longestConsecutive2(nums: List[int]) -> int:
    mp = defaultdict(int)
    res = 0
    
    for num in nums:
        if not mp[num]:
            mp[num] = mp[num-1] + mp[num+1] + 1
            mp[num - mp[num-1]] = mp[num]
            mp[num+ mp[num+1]] = mp[num]
            res = max(res,mp[num])
            
    return res
print(longestConsecutive2(nums=[2, 20, 4, 10, 3, 4, 5]))

