class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s2 = s[::-1]
        s[:] = s2
        print(s)