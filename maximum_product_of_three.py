# maximum_product_of_three.py
class Solution:
  def maximum_product_of_three(self, lst):
    product_list = []
    for i in range(len(lst)):
      for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
          max_product = lst[i] * lst[j] * lst[k]
          product_list.append(max_product)

    _max = max(product_list)
    return _max

  #   Minified Solution
  def maximum_product_of_threes(self, lst):
    product_list = [lst[i] * lst[j] * lst[k] for i in range(len(lst)) for j in range(i + 1, len(lst)) for k in
                    range(j + 1, len(lst))]

    _max = max(product_list)
    return _max


def main():
  lst = [-4, -4, 2, 8]
  print(Solution().maximum_product_of_three(lst))


main()
