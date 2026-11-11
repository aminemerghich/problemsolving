'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]  
        :rtype: List[List[str]]
        """
        my_map = {}

        for value in strs:
            sorted_s = ''.join(sorted(value))

            if sorted_s not in my_map:
                my_map[sorted_s] = []

            my_map[sorted_s].append(value)

        return list(my_map.values())
