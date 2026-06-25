class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if nums[0] != 0:
            return 0

        expected = 0

        for num in nums:
            if num != expected:
                return expected
            expected += 1

        return expected