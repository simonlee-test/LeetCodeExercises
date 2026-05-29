import re

#reversed string tc n sc n
def isPalindrome(s: str) -> bool:
    clean_string = re.sub(r"\W+", "", s.lower())
    reversed_s = clean_string[::-1]
    
    return clean_string == reversed_s

print(isPalindrome("Was it a car or a cat I saw?"))


# two pointer tc n sc 1
def isPalindrome1(s: str) -> bool:
    clean_string = re.sub(r"\W+", "", s.lower())
    reversed_s = clean_string[::-1]

    return clean_string == reversed_s


print(isPalindrome1("Was it a car or a cat I saw?"))
