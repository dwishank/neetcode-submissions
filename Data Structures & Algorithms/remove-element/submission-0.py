class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            
            if(nums[i] == val):
                nums.pop(i)
                print(nums)
                count = count + 1
            else:
                print("else")

        print(nums)
        while(count > 0):
            count = count - 1
        print(nums)
        return(len(nums))
            # if(nums[i] == val):

        #         print(nums)
        #         nums.pop(val)
        #         count += 1
        #     else:
        #         i = i + 1
        # return(count)