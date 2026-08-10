class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1 = nums
        nums1 = nums1 + nums1
        return nums1
        