def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    open =[]
    parenthesisDict = {"(":')', "[":']', "{":'}'}

    for i in s:
        #if i is an open parenthesis, append it to the stack
        if i in parenthesisDict.keys():
            open.append(i)
        
        #if i is a closing parenthesis
        elif i in parenthesisDict.values():
            #if the stack is empty
            if open ==[]:
                return False
            
            #if the parenthesises do not match
            elif parenthesisDict[open.pop()] != i:
                return False

    #if there is any hanging open parenthesis,        
    if len(open) !=0:
                return False

    #if it passes all the checking.    
    return True


s = "(([]))"
# s = "()[]{}"
print(isValid(s))


