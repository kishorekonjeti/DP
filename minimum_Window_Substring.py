from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        t = Counter(t)

        required = len(t)

        start, end = 0, 0

        count = 0

        candidate = dict()

        res = None
        
        filters = []
        
        for i in range(len(s)):
            if s[i] in t:
                filters.append((i, s[i]))
        
        while end < len(filters):
            
            character = filters[end][1]
            candidate[character] = candidate.get(character, 0) + 1

            if character in t and candidate[character] == t[character]:
                count += 1

            while start <= end and count == required:
                
                character = filters[start][1]
                left = filters[start][0]
                right = filters[end][0]
                
                
                if res == None or len(res) > len(s[left:right+1]):
                    res = s[left:right+1]

                candidate[character] -= 1
                if character in t and candidate[character] < t[character]:
                    count -= 1
                start += 1    

            end += 1    
        return "" if res == None else res
s =   Solution()
print(s.minWindow('ADOBECODEBANC','ABC'))




