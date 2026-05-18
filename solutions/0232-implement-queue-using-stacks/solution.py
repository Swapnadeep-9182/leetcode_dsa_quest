class MyQueue:

    def __init__(self):
        # Stack 1: Our Input Room (where new people join the line)
        self.stack1 = []
        # Stack 2: Our Output Room (where we serve the oldest people)
        self.stack2 = []

    def push(self, x: int) -> None:
        # New guy joins? Just throw him in Stack 1. Super fast! O(1)
        self.stack1.append(x)

    def pop(self) -> int:
        # We need to serve someone. Is Stack 2 empty?
        if not self.stack2:
            # If yes, bring everyone from Stack 1 into Stack 2 (reversing their order)
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Serve the guy at the top of Stack 2
        return self.stack2.pop()

    def peek(self) -> int:
        # Who is next in line? 
        # Same logic as pop, we need to make sure the oldest guy is ready in Stack 2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Just look at him, don't remove him! In Python, [-1] gets the last element (top of the stack)
        return self.stack2[-1]

    def empty(self) -> bool:
        # The momo stall is only empty if BOTH rooms are completely empty
        return not self.stack1 and not self.stack2
