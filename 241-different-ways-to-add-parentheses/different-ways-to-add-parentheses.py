class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []

        # Base case: string is empty
        if len(expression) == 0:
            return res
        
        # Base case: string is a single character, treat it as a number and return it
        if len(expression) == 1:
            return [int(expression)]
        
        # If string has 2 character, and first char is a digit, 2nd char must also be a digit(operations require >= 3)
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]
        
        # Recursive case: iterate through each character
        for i, current_char in enumerate(expression):
            
            # skip if curr char is a digit
            if current_char.isdigit():
                continue
            
            # split the expression into left and right parts
            left_res = self.diffWaysToCompute(expression[:i])
            right_res = self.diffWaysToCompute(expression[i + 1:])

            # combine res from left and right parts
            for left_value in left_res:
                for right_value in right_res:
                    if current_char == "+":
                        res.append(left_value + right_value)
                    elif current_char == "-":
                        res.append(left_value - right_value)
                    elif current_char == "*":
                        res.append(left_value * right_value)
            
        return res