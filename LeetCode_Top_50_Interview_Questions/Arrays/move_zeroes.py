"""
8. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        write_pointer = 0
        for read_pointer in range(0,len(nums)):
            if nums[read_pointer] != 0:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
        for j in range(len(nums)-1, write_pointer-1, -1):
            nums[j] = 0

        return nums
