"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.i
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set(nums)
        if (len(my_set) == len(nums)):
            return False
        return True
