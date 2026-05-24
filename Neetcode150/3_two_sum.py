# sorting - tc n log n, sc n
def twoSum(self, nums: list[int], target: int) -> list[int]:
    A = []
    for i, num in enumerate(nums):
        A.append([num, i])

    """ 
    it sorts them lexicographically
    
    It compares the first elements (index 0) of the sub-lists.

    If those first elements are different, it uses them to determine the order.

    If the first elements are a tie, it automatically moves on to compare the second elements (index 1) to break the tie, and so on.
    """

    A.sort()

    # two pointer at each end, when < target, increment i to bigger number, vice versa for j
    i, j = 0, len(nums) - 1

    while i < j:
        cur = A[i][0] + A[j][0]
        if cur == target:
            # ensure the result is in ascending order
            return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
        elif cur < target:
            i += 1
        else:
            j -= 1
    return []


print(twoSum([3, 4, 5, 6], 7))


# Hash map (two pass) tc n, sc n
def twoSum1(self, nums: list[int], target: int) -> list[int]:
    indices = dict()

    for i, num in enumerate(nums):
        indices[num] = i

    for i, num in enumerate(nums):
        diff = target - num

        if diff in indices and indices[diff] != i:
            return [i, indices[diff]]

    return []


print(twoSum([3, 4, 5, 6], 7))


# Hash map (one pass) tc n, sc n
def twoSum2(self, nums: list[int], target: int) -> list[int]:
    indices = dict()

    for i, num in enumerate(nums):
        diff = target - num
        if diff in indices:
            return [indices[diff], i]
        indices[num] = i 
    return []

print(twoSum([3, 4, 5, 6], 7))
