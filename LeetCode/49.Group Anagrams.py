#leet code 49.Group Anagrams

class Solution:
    def groupAnagrams(strs):
        sorted_strs = []
        for i in strs:
            s = ''.join(sorted(i))
            sorted_strs.append(s)
        unique = list(set(sorted_strs))
        
        res = []
        for j in unique:
            group = list(filter(lambda x: sorted_strs[x] == j, range(len(sorted_strs))))
            for k in range(len(group)):
                group[k] = strs[group[k]]
            res.append(sorted(group))

        return res

