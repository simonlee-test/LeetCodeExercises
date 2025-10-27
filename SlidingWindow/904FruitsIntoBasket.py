from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        max_len = 0
        fruit_count = defaultdict(int)

        #iterate from 0 to len(fruits)-1
        for end in range(len(fruits)):
            # increase the count of the respective fruit, to track the types of fruits
            fruit_count[fruits[end]] += 1

            # when more than 2 types of fruits,
            while len(fruit_count) > 2:
                # delete one type of fruit completely to start the next cycle.
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]] #this will be the stopping point
                start += 1
                
            # This would serve a record for max_len for 2 types of fruits, it would compare every iteration until the for loop ends.
            max_len = max(max_len, end - start + 1)

        return max_len

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        # https://leetcode.com/problems/fruit-into-baskets/
        
        # This problem is similar to Longest Substring Without Repeating Characters.
        # The only difference is that we have to find the longest substring with 2 distinct characters.
        
""" 
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 
"""