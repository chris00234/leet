class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = set()

        q = deque(["0000"])
        moves = 0

        while q:
            for _ in range(len(q)):
                state = q.popleft()
                if state == target:
                    return moves
                if state in seen or state in deadends:
                    continue
                seen.add(state)
                for i in range(len(state)):
                    char = int(state[i])
                    pChar = str((char + 9) % 10)
                    nChar = str((char + 1) % 10)
                    pState = state[:i] + pChar + state[i+1:]
                    nState = state[:i] + nChar + state[i+1:]
                    q.append(pState)
                    q.append(nState)
            moves += 1
            
        return -1
