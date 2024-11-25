class Solution:
    def slidingPuzzle(self, board):
        # Directions for possible swaps based on '0' position
        dir = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        target = "123450"
        vis = set() # Track visited configurations
        q = deque()
        start = ""

        # Convert 2D board to a single string
        for row in board:
            for col in row:
                start += str(col)

        q.append(start)
        vis.add(start)
        step = 0

        # Perform BFS
        while q:
            size = len(q)
            for _ in range(size):
                current = q.popleft()

                # Check if target is reached
                if current == target:
                    return step

                zero = current.find('0') # Find position of '0'

                # Generate next moves
                for move in dir[zero]:
                    next_state = list(current)
                    next_state[zero], next_state[move] = next_state[move], next_state[zero]
                    next_state = ''.join(next_state)
                    if next_state not in vis:  # Add unvisited states to the queue
                        vis.add(next_state)
                        q.append(next_state)
            step += 1
        return -1  # Return -1 if target is unreachable
