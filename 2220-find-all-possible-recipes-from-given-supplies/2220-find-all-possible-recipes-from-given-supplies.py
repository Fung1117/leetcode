class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        recipes_ingredients = { recipes[i]: set(ingredients[i]) for i in range(n) }
        supplies = set(supplies)
        allsupplies = []
        isModified = True

        while isModified:
            isModified = False
            newRecipe = []
            for recipe in recipes_ingredients:
                ingredient = recipes_ingredients[recipe]
                if ingredient.issubset(supplies):
                    newRecipe = recipe
                    allsupplies.append(recipe)
                    isModified = True
                    break
            if isModified:
                supplies.add(newRecipe)
                del recipes_ingredients[newRecipe]

        return allsupplies

