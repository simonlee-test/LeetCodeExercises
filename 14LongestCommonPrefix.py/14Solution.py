from typing import *
def longestCommonPrefix(strs: List[str]) -> str:
        """
        If the array is sorted alphabetically then you can assume that the first element of the array and the last element of the array 
        will have most different prefixes of all comparisons that could be made between strings in the array. 
        If this is true, you only have to compare these two strings.
        For example, "bark alligator barn" would be sorted as "alligator bark barn"

        """
        prefix=""

        #the array is sorted alphabetically
        strs=sorted(strs)
       
        first=strs[0] #first element
        last=strs[-1] #last element

        print(min(len(first),len(last)))

        #the length of index decide by the shortest string between first and last
        #if the array string is empty, this for loop will not run.
        for i in range(min(len(first),len(last))):
            #if there is unmatch char, return current stored prefix
            if(first[i]!=last[i]):
                return prefix
            
            #else, append current character to prefix
            prefix+=first[i]

        return prefix #to return when the list passed in is empty

strs = ["dog","dongle","door","dodge"] #--> min(len('dodge'),len('door')) =4

print (longestCommonPrefix(strs))

for i in range(0):
     print('hello')