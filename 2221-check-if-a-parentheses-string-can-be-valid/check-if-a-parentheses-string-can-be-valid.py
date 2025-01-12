class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        # number of opening and closing brackets are equal = string is balanced
        open_brackets = deque()
        unlocked = deque()

        for i in range(n):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                open_brackets.append(i)
            elif s[i] == ')':
                if open_brackets:
                    open_brackets.pop()
                elif unlocked: # use an unlocked position and pop it to match
                    unlocked.pop()
                else:
                    return False
        
        # Match remaining open brackets and the unlocked characters
        # last condition is to preserve the order of a valid parentheses string 
        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()
        
        # we only check if open_brackets is empty as number of parentheses left in unlocked is guranteed to be even
        if open_brackets:
            return False
        
        return True