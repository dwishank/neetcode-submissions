class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = {}
        c = {}
        for i in s:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        for j in t:
            if j in c:
                c[j] += 1
            else:
                c[j] = 1    
        if(b == c):
            return True
        else:
            return False
