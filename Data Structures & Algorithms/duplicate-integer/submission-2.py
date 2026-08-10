class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len1 = len(nums)
        fre = {}
        vare = False
        for i in nums:
            if i not in fre:
                fre[i] = 1
            else:
                fre[i] += 1
                vare = True
                
        if(vare == False):
            return False
        else:
            return True


        