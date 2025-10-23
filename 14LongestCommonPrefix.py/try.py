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
            #if one of the string is empty
            if i=="":
                flag=False
                prefix.pop()
                break
            #if the index is longer than the shortest string
            if index == len(i):
                flag = False
                #if this is not the last string
                if count != len(strs)-1:
                    prefix.pop()
                break

            if i[index] != prefix[index]:
                flag=False
                prefix.pop()
                break
            elif count == len(strs)-1:
                if index == len(i)-1:
                    flag = False
                    break
                print(i[index+1])
                prefix.append(i[index+1])
            count +=1
        index+=1
    return "".join(prefix)

strs = ["abab","aba",""]
print (longestCommonPrefix(strs))


