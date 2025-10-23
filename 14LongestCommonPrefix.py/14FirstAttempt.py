def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs)!=0 and len(strs[0])!=0:
        prefix = [strs[0][0]]
    else:
        return ""
    flag = True
    index=0

    while flag:
        count=0
        for i in strs:
            #if one of the string is empty, added index ==0 is to ensure that this test 
            # only run at the first round only
            if i=="" and index==0:
                flag=False
                prefix.pop()
                break
            #if the index is longer than the shortest string
            if index == len(i):
                flag = False
                #if this is not the last string, pop the prefix.
                # because if it is last string, it 
                # would have been check in line 40 already
                if count != len(strs)-1:
                    prefix.pop()
                break

            #if not equal prefix   
            if  (i[index] != prefix[index]):
                flag=False
                prefix.pop() #take out because not match ald
                break
            
            #if last string in the list already, means that prefix already pass all the tests in 
            #other strings
            if count == len(strs)-1:
                #if last index alread, this is to prevent string out of index error for the append later.
                if index == len(i)-1:
                    flag = False
                    break
                # print(i[index+1])
                prefix.append(i[index+1])

            #proceed to next string after finish checking on string
            count +=1
        #proceed to next character, iterate all the strings in the list again
        index+=1

    return "".join(prefix)

strs = ["abab","aba",""]
print (longestCommonPrefix(strs))


