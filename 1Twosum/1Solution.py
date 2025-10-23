def twoSum(nums, target):
    pairDict ={}
    for i,n in enumerate(nums):
        #if n is found as a partner of other numbers to form target,
        if n in pairDict:
            #return partner index, current num index
            return pairDict[n], i
        
        else:
            #map the needed partner to current index
            pairDict[target-n] =i
    return None # default return none

print(twoSum([4,3,7,13,3], 69))