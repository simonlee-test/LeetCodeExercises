def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    open =[]
    parenthesisDict = {"(":')', "[":']', "{":'}'}

    for i in s:
        #if i is an open parenthesis, append it to the stack
        if i in parenthesisDict:
            open.append(i)
        
        #if i is an closing parenthesis, 
        elif i in parenthesisDict.values():
            #if the stack is empty or the open and closing parenthesises do not match
            if open ==[] or parenthesisDict[open.pop()] != i:
                return False

    #if there is any hanging open parenthesis, this return False, else true        
    return len(open) ==0


s = "(([]))"
# s = "()[]{}"
print(isValid(s))


