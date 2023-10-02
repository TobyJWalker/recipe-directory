from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe.sql")

# find the recipe with id 3
recipe_repo = RecipeRepository(connection)

recipe = recipe_repo.find(3)
print(recipe)