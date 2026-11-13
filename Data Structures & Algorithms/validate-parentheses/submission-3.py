class Solution:
    def isValid(self, s: str) -> bool:
        
        key_map={
            ")":"(",
            "}":"{",
            "]":"["
            }
        
        stack=[]
        
        for char in s:
            if char in key_map:
                val=key_map[char]
                if stack and stack[-1]==val:
                    stack.pop()
                else:
                    return False            
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True