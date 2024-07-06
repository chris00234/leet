class Solution:
    def removeStars(self, s: str) -> str:
        queue = []
    
        for char in s:
            if char == "*" and len(queue) >= 1:
                queue.pop(-1)
            else:
                queue.append(char)
        return "".join(queue)
