class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack == [] or i not in ["}", ")", "]"]:
                stack.append(i)
                print(i)
            elif stack[-1] == "{" and i == "}":
                stack.pop()
            elif stack[-1] == "(" and i == ")":
                stack.pop()
            elif stack[-1] == "[" and i == "]":
                stack.pop()
            elif stack[-1] == "(" and i != ")":
                return False
            elif stack[-1] == "{" and i != "}":
                return False
            else:
                return False
        
        if stack == []:
            return True
        else:
            return False
            