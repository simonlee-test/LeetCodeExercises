def romanToInt(s):
    """
    :type s: str
    :rtype: int
    Contraints:
        s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        It is guaranteed that s is a valid roman numeral in the range [1, 3999]
    Comments: it works, but it is abusing the try-catch in flow control, we need to use if else
    """

    total = 0
    romanDict={"I":1,"V":5,'X':10,'L': 50,'C':100,'D':500,'M':1000, 'IV':4, 'IX':9,
           'XL':40, 'XC':90,'CD':400,'CM':900}
    i=0

    while i < len(s):

        #to prevent string out of index error and fail to find the key when romanDict[pair], if either of this happens, implying that there is no 4,9,40,90,400,900, it will jump to except.
        try:
            pair= s[i]+s[i+1]
            print("pair here "+pair+f' added value {romanDict[pair]}')   
            total += romanDict[pair]
            i = i+2 #plus 2 to skip the following value, because this is while loop, +1 means next number,
                    #+2 means skip the next number, go to the number after the next number.
     
        except:
            print(f"solo value {s[i]} except value {romanDict[s[i]]}")
            total += romanDict[s[i]]
            i +=1 
    
    return total

#test cases
s = "MCMXCIV"
# print(romanToInt("MCMXLIX"))
# print(romanToInt(s))
print(romanToInt("III"))

#original 
# total = 0
# romanDict={"I":1,"V":5,'X':10,'L': 50,'C':100,'D':500,'M':1000, 'IV':4, 'IX':9,
#            'XL':40, 'XC':90,'CD':400,'CM':900} 
# i=0

# while i < len(s):
#     #to prevent out of string error
#     try:
#         pair= s[i]+s[i+1]
#     except:
#         pass

#     try:
#         if romanDict[pair]:
#             print("pair here "+pair+f' added value {romanDict[pair]}')   
#             total += romanDict[pair]
#             i = i+2 #plus 2 to skip the following value, because this is while loop, +1 means next number,
#                     #+2 means skip the next number, go to the number after the next number.
               
#     except:
#         print(f"solo value {s[i]} except value {romanDict[s[i]]}")
#         total += romanDict[s[i]]
#         i +=1

# print(total)



    
