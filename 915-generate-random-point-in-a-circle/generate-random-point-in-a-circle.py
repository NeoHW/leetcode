class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        x_start, x_end = self.x_center - self.radius, self.x_center + self.radius
        y_start, y_end = self.y_center - self.radius, self.y_center + self.radius
        while True:
            x, y = random.uniform(x_start, x_end), random.uniform(y_start, y_end)
            if (x - self.x_center)**2 + (y - self.y_center)**2 <= self.radius**2:
                return [x,y]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()