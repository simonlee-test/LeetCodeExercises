"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""

class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
      left = right = 0
      max_length = 0
      # starting from 0 to the end of the array
      for right in range(len(A)):
        # decrement k when encounter zero
        if A[right] == 0:
          K -= 1
        
        # when k hit negative, means that we are running out of zeros
        if K < 0:
          # if the starting point of the window is 0, reclaim a k
          if A[left] == 0:
            K += 1
          # move the starting point of a window.
          left += 1

        #record the max length
        max_length = max(max_length, right - left + 1)
      
      return right - left + 1
            