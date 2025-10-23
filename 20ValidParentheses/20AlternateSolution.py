
def isValid(s: str) -> bool:
    stack = []
    parenthesisDict = {')': '(', '}': '{', ']': '['}
    for c in s:
        #if it is a closing parenthesis
        if c in parenthesisDict:
            #assign top to stack.op() if stack is empty then assign a value'#'
            top = stack.pop() if stack else '#'

            #compare their values
            if parenthesisDict[c] != top:
                return False
        #if it is an open parenthesis
        else:
            #add the open parenthesis to the stack
            stack.append(c)
    #if it is empty, return true
    return not stack
    
s = "(([]))"
# s = "()[]{}"
print(isValid(s))