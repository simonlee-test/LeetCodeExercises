from typing import *
def longestCommonPrefix(strs: List[str]) -> str:
    """
    Initialize an empty string. Zip the list, so you get the first characters of each word together in a tuple, 
    the second letters in another tuple, and so on. Convert each such tuple into a set, 
    and check if the length of the set is 1 - to understand if the elements were same (as sets store only 1 instance of a repeated element).
    If the length of the set is 1, add the first element of the tuple (any element is fine, 
    as all elements are same but we take the first element just to be cautious) to the empty string. 
    If the length of a set is not 1 (means that there are more than one element appear during comparison a.k.a diff string already), 
    return the string as is. Finally, return the string obtained thus far.
    """
    prefix = ""
    #zip(*strs) is used to unpack the elements of a list of iterables. 
    #Specifically, *strs is used to pass each string in the strs list as a separate argument to the zip() function. 
    #So its the equivalent of zip(str1, str2, str3) and strings are basically list of characters. 
    #so it will output something like zip([hello, dog, cat]) => [(h, d, c), (e, o ,g) ...]

    for char in zip(*strs):
        #use set to check if there is more than one character appear at each position.
        #if len (set(char)) ==1 means that there is only one character.
        print(char) 
        
        if len(set(char)) == 1:
            print(char) 
            prefix += char[0]
        else: 
            return prefix
    return prefix

strs = ["dog","dongle","door","dodge"] 

print (longestCommonPrefix(strs))

for i in range(0):
     print('hello')