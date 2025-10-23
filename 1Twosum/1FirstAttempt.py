def twoSum(nums, target):
    lastIndex = len(nums)
    result =[]

    for i in range(0,lastIndex):
        partner = target - nums[i]
        try:
            partnerIndex = nums.index(partner,i+1)
            if partnerIndex:
                result.append(i)
                result.append(partnerIndex)
                return result
        except:
            pass
    return 0

print(twoSum([4,3,7,13,3], 6))