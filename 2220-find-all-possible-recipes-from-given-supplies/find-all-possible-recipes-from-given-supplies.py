class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # topological sort
        supplies_set = set(supplies)
        AL = defaultdict(list)
        in_degrees = {} 
        res = []

        for i,recipe in enumerate(recipes):
            in_degrees[recipe] = 0
            for ingredient in ingredients[i]:
                if ingredient not in supplies_set:
                    AL[ingredient].append(recipe)
                    in_degrees[recipe] += 1
    
        q = deque()
        for recipe in in_degrees:
            if in_degrees[recipe] == 0:
                q.append(recipe)
        
        while q:
            recipe = q.popleft()

            supplies_set.add(recipe)
            res.append(recipe)

            for neighbour in AL[recipe]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 0:
                    q.append(neighbour)
    
        return res
    