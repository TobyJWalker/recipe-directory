from lib.recipe_repository import RecipeRepository

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipe.sql")
    recipe_repo = RecipeRepository(db_connection)

    recipes = recipe_repo.all()

    assert len(recipes) == 5
    assert recipes[0].name == "Pizza"
    assert recipes[-1].name == "Burger"

def test_find_one_recipe(db_connection):
    db_connection.seed("seeds/recipe.sql")
    recipe_repo = RecipeRepository(db_connection)

    recipe_1 = recipe_repo.find(1)
    recipe_5 = recipe_repo.find(5)

    assert recipe_1.name == "Pizza"
    assert recipe_5.name == "Burger"
