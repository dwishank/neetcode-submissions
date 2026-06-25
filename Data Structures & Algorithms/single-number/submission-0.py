class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b = {}
        output = 0
        for i in nums:
            if i in b:
                b[i] +=1
            else:
                b[i] = 1
        for j in b:
            if(b[j] == 1):
                output = j

        return output