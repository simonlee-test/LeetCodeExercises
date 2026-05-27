from collections import defaultdict

#sorting tc m*n log n sc m* n
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    mappings = defaultdict(list)
    
    for string in strs:
        sorted_string = ''.join(sorted(string.lower()))
        mappings[sorted_string].append(string)
        
    return list(mappings.values())

strs = ["act", "pots", "tops", "cat", "stop", "hat"]

print(groupAnagrams(strs))

#hash table
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())

