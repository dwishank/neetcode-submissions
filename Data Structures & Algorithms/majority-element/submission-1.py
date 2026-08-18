class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nam = {}
        for i in nums:
            if i not in nam:
                nam[i] = 1
            else:
                nam[i] += 1
        return(max(nam, key=nam.get))
        
            
        