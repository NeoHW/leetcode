class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colours = {}
        colour_count = {}
        res = []

        for ball, new_colour in queries:
            if ball in ball_colours:
                colour = ball_colours[ball]
                colour_count[colour] -= 1
                if colour_count[colour] == 0:
                    del colour_count[colour]

            ball_colours[ball] = new_colour
            if new_colour not in colour_count:
                colour_count[new_colour] = 0
            colour_count[new_colour] += 1
        
            res.append(len(colour_count))
        
        return res