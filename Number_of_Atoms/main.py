class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i, n = 0, len(formula)
        # Initialize a counter to keep track of the atoms
        count = Counter()
        stack = [count]

        # Loop through the formula
        while i < n:
            # '(' indicates the start of a new formula
            if formula[i] == '(':
                i += 1
                # Initialize a new counter for the new formula
                count = Counter()
                # Add the new counter to the stack
                stack.append(count)
            # ')' indicates the end of a formula
            elif formula[i] == ')':
                i += 1
                # Find the end of the count that follows the ')'
                end = i
                while i < n and formula[i].isdigit():
                    i += 1
                # Get the count, default to 1 if no count is provided
                mult = int(formula[end:i] or 1)
                top = stack.pop()
                # Add the count of each atom in the popped counter to the top counter in the stack
                for name, v in top.items():
                    stack[-1][name] += v * mult
                # Update the current counter to the top counter in the stack
                count = stack[-1]
            else:
                # If the current character is not '(' or ')', it's an atom
                # Find the end of the atom name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                # Get the atom name
                name = formula[start:i]
                # Find the end of the count that follows the atom name
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                # Get the count, default to 1 if no count is provided
                mult = int(formula[start:i] or 1)
                # Add the count of the atom to the top counter in the stack
                stack[-1][name] += mult

        # Return the count of all atoms in the format specified in the problem
        return "".join(name + (str(count[name]) if count[name] > 1 else '') for name in sorted(count))
