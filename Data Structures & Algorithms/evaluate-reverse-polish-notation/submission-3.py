import operator
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        # Mapping operators to functions speeds up lookup and execution over if/elif
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            # Integer-only truncation toward zero without float precision bugs
            "/": lambda a, b: int(a / b) 
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
                
        return stack[0]