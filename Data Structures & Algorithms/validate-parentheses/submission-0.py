class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for pran in s:
            if pran == '[' or pran == '(' or pran == '{':
                stack.append(pran)
                
            elif pran == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
                
            elif pran == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()

            elif pran == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
                
        
        if len(stack) == 0:
            return True
        else:
            return False