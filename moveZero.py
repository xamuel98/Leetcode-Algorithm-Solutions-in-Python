# moveZeros.py
class Solution:
  '''Create a function with parameters nums (the list to be passed) and another list
    list2 initially empty
  '''
  def moveZeros(self, nums, list2=[]):
    '''In order to eliminate the issue of list index out of range create a
    list object, passing the list - nums variable as an argument
    '''
    res_list = list(nums)
    # Loop through the list - nums
    for i in range(len(nums)):
      # If an element of the list - nums equals 0
      if nums[i] == 0:
        # Append the 0s the initially empty created list
        list2.append(nums[i])
        # Once the 0s are appended to the new list - list2, remove them the old list - res_list
        res_list.remove(nums[i])

    # Add the new list - list, to the old list
    res_list.extend(list2)

    # Return the updated list
    return res_list

def main():
  nums = [0,0,0,2,0,1,3,4,0,0]
  # print(Solution().moveZeros(nums))
main()
