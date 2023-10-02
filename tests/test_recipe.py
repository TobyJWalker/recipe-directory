from lib.recipe import Recipe

def test_recipe_initalise():
    recipe = Recipe(1, "Test Recipe", 1, 2)

    assert recipe.name == "Test Recipe"
    assert recipe.cooking_time == 1
    assert recipe.rating == 2

def test_repr():
    recipe = Recipe(1, "Test Recipe", 1, 2)

    assert str(recipe) == "Recipe(1, Test Recipe, 1, 2)"

def test_eq():
    recipe = Recipe(1, "Test Recipe", 1, 2)
    recipe2 = Recipe(1, "Test Recipe", 1, 2)
    
    assert recipe == recipe2