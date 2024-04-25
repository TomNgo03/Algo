def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    dict = {}
    
    for w in strs:
        n = ''.join(sorted(w))
    
    if n in dict:
        dict[n] += [w]
    
    else:
        dict[n] = [w]
    
    return list(dict.values())
    