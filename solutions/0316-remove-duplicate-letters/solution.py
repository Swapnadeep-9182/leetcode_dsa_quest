class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurence = {char : i for i, char in enumerate(s)}
        stack = []
        seen = set()
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and char < stack[-1] and last_occurence[stack[-1]] > i:
                kicked_out = stack.pop()
                seen.remove(kicked_out)
            stack.append(char)
            seen.add(char)
        return "".join(stack)
