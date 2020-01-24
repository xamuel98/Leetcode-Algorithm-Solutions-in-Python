# Program that prints k largest elements in an array
class Solution:
  def kthLargestElement(self, nums, k):
    nums.sort(reverse=True)
    for i in range(k):
      print(nums[i], end=" ")


def main():
  (Solution().kthLargestElement([1,23,12,9,30,2,50],3))
main()
