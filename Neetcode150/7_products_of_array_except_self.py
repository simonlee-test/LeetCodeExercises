from typing import List

# division tc n sc n
def productExceptSelf(nums: List[int]) -> List[int]:
    total = nums[0]
    zero_count = 0
    
    for num in nums[1:]:
        if num == 0:
            zero_count+=1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        if total != 0 and num != 0:
            total *= num
    
    res = []
    
    if zero_count==0:
        for num in nums:
            res.append(int(total/num))
    else:
        res= [0] * len(nums)   
        zero_index = nums.index(0)
        res[zero_index] = int(total)
    
    return res


# prefix suffix
def productExceptSelf1(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    
    prefix = 1
    
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    postfix = 1
                                # the stopping index is exclusive, now is -1, means till 0 only
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res

print(productExceptSelf1([1, 2, 4, 6]))