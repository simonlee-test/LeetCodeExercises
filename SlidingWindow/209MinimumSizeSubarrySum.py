class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_length = len(nums) + 1
        start = 0

        for end in range(len(nums)):
            # Decrease target value from start
            target -= nums[end]

            # When greater than target value
            while target <= 0:
                # Compare min with current array length
                min_length = min(min_length, end - start + 1)
                # Offset the value of the initial element
                target += nums[start]
                # Move to the next element
                start += 1

        return 0 if min_length > len(nums) else min_length


solution = Solution()
print(solution.minSubArrayLen(4, [1, 4, 4]))

# Amortized Analysis -- Write off the initial cost of computation gradually -- average out the impact of worst case scenario
# https://leetcode.com/problems/minimum-size-subarray-sum/solutions/433123/java-c-python-sliding-window
"""
Time Complexity: O(N)
- The time complexity is linear because of amortized analysis, which accounts for the total work done over the entire process, not just the work within a single loop iteration.
- Outer Loop (Pointer end): The for end in range(len(nums)) loop executes exactly N times. The end pointer advances one step at a time, performing O(1) work in each step before the inner loop check.
- Inner Loop (Pointer start): The while target <= 0: loop advances the start pointer.
  - The start pointer never moves backward.
  - It starts at index 0 and can advance to N at most.
  - Therefore, the total number of times the inner while loop executes across the entire run of the algorithm is bounded by N.
  - Since both pointers (start and end) make at most N total movements, the overall number of operations is proportional to N + N, which simplifies to O(N).

Space Complexity: O(1)
- The space complexity is constant because the algorithm uses only a fixed number of extra variables: min_length, start, target (which holds a running sum), and loop counter end.
- The memory used by these variables does not grow with the size of the input array nums.
"""
