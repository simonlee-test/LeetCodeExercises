from typing import List

nums = [1,2,3,3]

#sorting - TC n log n, SC n
def hasDuplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    
    return False

#hash set length - n
def hasDuplicate1(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
            
print(hasDuplicate1(nums))  

#hash set - n
def hasDuplicate2(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(hasDuplicate2(nums))
