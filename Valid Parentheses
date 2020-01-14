class Solution:
    def isValid(self, s: str) -> bool:
        stack, open_list, close_list = [], ["(", "[", "{"], [")", "]", "}"]
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                position = close_list.index(i)
                if (len(stack) > 0) and open_list[position] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
