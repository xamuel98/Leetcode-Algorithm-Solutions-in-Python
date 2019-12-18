class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        see = {}
        for key,value in enumerate(nums):
          num = target - value
          if num not in see:
            see[value] = key
          else:
            return [see[num],key]
