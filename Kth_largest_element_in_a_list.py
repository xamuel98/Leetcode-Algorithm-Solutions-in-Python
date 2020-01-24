# Kth_largest_element_in_a_list.py
class Solution:
  def findKthLargest(self, nums, k):
    if k <= len(nums):
      nums.sort(reverse=False)
    else:
      raise ValueError("K has exceeded the length of the list")

    return nums[-k]


def main():
  print(Solution().findKthLargest([1,23,12,9,30,2,50],3))
 main()
