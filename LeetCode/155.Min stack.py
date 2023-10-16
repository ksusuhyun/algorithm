#leet code 155.Min stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if not self.stack :
            self.stack.append(val)
            self.min_stack.append(val)

        else :
            if val < self.min_stack[-1] :
                self.stack.append(val)
                self.min_stack.append(val)
            else :
                self.stack.append(val)
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]