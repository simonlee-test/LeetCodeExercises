def romanToInt(s):
    """
    :type s: str
    :rtype: int
    Contraints:
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        It is guaranteed that s is a valid roman numeral in the range [1, 3999]
    Comments: this is the correct solution using hash table by utilizing substraction algorithm as requested. Solution from leetcode
 
    """

    total = 0
    romanDict={"I":1,"V":5,'X':10,'L': 50,'C':100,'D':500,'M':1000}

    for i in range(len(s)):
        #if i is not the last index (to prevent string out of index error) and if romanDict[s[i]] < romanDict[s[i+1]]
        if i < len(s) -1 and romanDict[s[i]] < romanDict[s[i+1]]:
            total -= romanDict[s[i]]
     
        else:
            total += romanDict[s[i]]
    
    return total

#test cases
s = "MCMXCIV"
# print(romanToInt("MCMXLIX"))
# print(romanToInt(s))
print(romanToInt(s))
