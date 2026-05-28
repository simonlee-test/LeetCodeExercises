from typing import List

delimiter = "::"
length_delimiter = '||'
def encode(strs: List[str]) -> str:
    lengths=''
    words=''
    
    for i, string in enumerate(strs):
        lengths += '||' + str(len(string))
        words+=string
    
    result = delimiter.join([words, lengths])

    return result

def decode(s: str) -> List[str]:
    words, lengths = s.split(delimiter)
    lengths = lengths.split(length_delimiter)[1:]
    res=[]
    
    for length in lengths:
        length= int(length)
        word = words[:length]
        words = words[length:]
        res.append(word)
    
    return res

password = encode(["we", "say", ":", "yes", "!@#$%^&*()"])
password = decode(password)

print(password)

def encode(strs: List[str]) -> str:
    res=""
    for s in strs:
        res += str(len(s)) + '#' + s
    return res
    
def decode(s: str) -> List[str]:
    res =[]
    i = 0
    
    while i < len(s):
        # starting point
        j = i
        while s[j] != '#':
            j+=1
        
        length = int(s[i:j])
        
        # skip the # delimiter and reset starting point
        i = j+1
        
        j = i + length
        
        res.append(s[i:j])

        # reset starting point
        i = j
        
    return res