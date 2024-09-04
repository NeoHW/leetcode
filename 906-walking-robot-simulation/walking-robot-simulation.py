class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = {(x, y) for x, y in obstacles}
        max_distance_squared = 0
        x,y = 0,0
        
        curr_direction = 0
        # 0 for north, 1 for east, 2 for south , 3 for west
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for command in commands:
            if command == -2:
                curr_direction = (curr_direction + 4 - 1) % 4
            elif command == -1:
                curr_direction = (curr_direction + 1) % 4
            else:
                dx, dy = directions[curr_direction]
                for _ in range(command):
                    newx = x + dx
                    newy = y + dy
                    if (newx, newy) in obstacle_set:
                        break
                    x,y = newx, newy
                    max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared