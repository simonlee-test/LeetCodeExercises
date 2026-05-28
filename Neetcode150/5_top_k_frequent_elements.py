from typing import List
from collections import defaultdict
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = defaultdict(int)
    count = 0
    sorted_nums = []
    
    for n in nums:
        res[n] +=1
    
    while count < k:
        target = (nums[0], res[nums[0]])
        for key, value in res.items():
            if value > target[1]:
                target = (key, value)
        sorted_nums.append(target[0])
        res.pop(target[0])
        count+=1
        
    return sorted_nums


#sorting tc n log n sc n
""" 
To understand why sorting takes U log U steps, we have to look at how a computer actually sorts things. A computer cannot look at all the cue cards at once like a human can. It can only compare two cards at a time. Here is exactly how we get to that number.

First, let us understand the log part, which is short for logarithm. In computer science, log U basically means: How many times do I have to cut a pile of U cards in half until I am left with just 1 card?

If you have 8 cards and keep splitting them in half:
In split 1, you have 4 cards.
In split 2, you have 2 cards.
In split 3, you have 1 card.
It took 3 steps to get down to 1 card. In math terms, log base 2 of 8 equals 3.

Second, let us look at how sorting works with divide and conquer. Python uses a sorting method called Timsort, which is based on Merge Sort. To sort a pile of U cards, the computer does the flipping game in reverse. It pretends your big pile of U cards is actually U tiny piles of just 1 card each, and a pile of 1 card is automatically sorted. It takes pairs of these tiny piles and merges them into sorted piles of 2. It takes those piles of 2 and merges them into sorted piles of 4. It keeps doing this until the whole pile is put back together.

Third, we put U and log U together. To figure out the total work, we multiply two things: the number of rounds and the work per round.

For the number of rounds, which is log U, the computer doubles the size of the piles in every round. Because of this, it only needs to do this merging process log U times before the whole deck is fully sorted. For 8 cards, it only takes 3 rounds of merging.

For the work per round, which is U, the computer has to look at and compare almost every single card in every single round to merge the piles correctly. If you have U cards total, it does about U steps of work per round.

To get the grand total, we multiply the work per round by the number of rounds, which gives us U times log U.

To see why this is efficient, look at how much better U log U is compared to a lazy sorting method, like checking every card against every other card, which takes U squared steps.

If you have 4 unique candies, simple sorting takes 16 steps while smart sorting takes 8 steps.
If you have 8 unique candies, simple sorting takes 64 steps while smart sorting takes 24 steps.
If you have 64 unique candies, simple sorting takes 4096 steps while smart sorting takes 384 steps.
If you have 1000 unique candies, simple sorting takes 1000000 steps while smart sorting takes 10000 steps.

As your candy pile grows, the log U trick saves the computer millions of steps!
"""
def topKFrequent1(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int)
    
    for num in nums:
        count[num] +=1
        
    arr = []
    
    for num, count in count.items():
        arr.append([count, num])
    
    arr.sort()
    
    result =[]
    
    for i in range(k):
        result.append(arr.pop()[1])
    
    return result

# minHeap - tc n log k, sc n + k
""" 
1. Time Complexity: O(nlogk) vs. O(nlogn)
The O(nlogk) approach is faster, especially when k is much smaller than n.

O(nlogn): This happens when you sort the entire list of n items. If you have 1,000,000 items, you have to sort all 1,000,000 of them.
O(nlogk): This usually happens when you use a tool called a Min-Heap to only track the top k items at any given time. Instead of sorting everything, you look at all n items one by one, but you only ever sort and manage a tiny pile of k items.
Why it matters: If n=1,000,000 and k=10, sorting the whole thing (nlogn) takes about 20 million operations. Using a min-heap (nlogk) only takes about 3.3 million operations. That is a massive speedup.
2. Space Complexity: O(n+k) vs. O(n)
The O(n) approach uses less memory.

O(n): This means the extra memory you need scales perfectly with the number of items you started with. If you are just sorting an array in place or building a simple frequency map, you only need space proportional to n.
O(n+k): This means you are using extra memory to hold both the original group of elements (n) and maintaining a separate data structure (like our heap or an extra array) of size k at the same time.
"""
#min heap keep track of the smallest frequency in the current so that we can kick it out when a larger one enter
# effectively, we are maintaining the top k most frequent elements since all the smaller ones have been kicked out.
# heap always sort based on the first element, unlike sorted where we can control with key= lambda
def topKFrequent2(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int)
    for num in nums:
        count[num] +=1
        
    heap = []
    for num, freq in count.items():
        #update the heap by inserting the element, the heap would sort with the first element it self
        heapq.heappush(heap, (freq, num))
        
        #prune the smallest freq one
        if len(heap) > k:
            heapq.heappop(heap)
    
    res = []
    for i in range(k):
        #get the respective numbers from the arranged freq
        res.append(heapq.heappop(heap)[1])
    
    return res

#bucket sort - tc n sc n
def topKFrequent3(nums: List[int], k: int) -> List[int]:
    count = defaultdict(int)
    freq = [ [] for i in range(len(nums)+ 1)]

    for num in nums:
        count[num] +=1
        
    for num, cnt in count.items():
        freq[cnt].append(num)
        
    res = []
    
    for i in range(len(freq) - 1, 0 , -1):
        for num in freq[i]:
            res.append(num)
            if len(res) >= k:
                return res
                

print(topKFrequent3([1, 2, 2, 3, 3], k=2))