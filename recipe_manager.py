import csv

from recipe import Recipe
from sorting import LoopSort, RecursiveSort
from logic import evaluate_recipe_logic


# The CSV file that stores all the recipes.
CSV_FILE = "recipes.csv"

# The column order we expect inside recipes.csv.
CSV_HEADER = ["name", "category", "price", "cooking_time", "ingredients", "calories"]


class RecipeManager:
    """Keeps the list of recipes and handles loading, saving and searching."""

    def __init__(self):
        # The list that holds all Recipe objects.
        self._recipes = []
        # Sorting helpers so the manager can sort by price or cooking time.
        self._loop_sorter = LoopSort()
        self._recursive_sorter = RecursiveSort()

    def get_recipes(self):
        return self._recipes

    def load_recipes(self):
        """Load recipes from the CSV file at program start."""
        self._recipes = []
        try:
            with open(CSV_FILE, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # If one row has bad data, skip it and keep going.
                    try:
                        recipe = Recipe(
                            row["name"],
                            row["category"],
                            row["price"],
                            row["cooking_time"],
                            row["ingredients"],
                            row["calories"],
                        )
                        self._recipes.append(recipe)
                    except (ValueError, KeyError, TypeError):
                        print("Skipping a row with invalid data.")
            print("Loaded", len(self._recipes), "recipes from", CSV_FILE)
        except FileNotFoundError:
            # Friendly message instead of crashing.
            print("File", CSV_FILE, "was not found. Starting with an empty list.")
            self._recipes = []

    def save_recipes(self):
        """Save all recipes back to the CSV file."""
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADER)  # write the header first
            for recipe in self._recipes:
                writer.writerow(recipe.to_row())
        print("Saved", len(self._recipes), "recipes to", CSV_FILE)

    def show_all(self):
        """Print a short line for every recipe."""
        if not self._recipes:
            print("There are no recipes to show.")
            return
        print("(* means the recipe is recommended)")
        for recipe in self._recipes:
            recipe.show_short()

    def add_recipe(self, recipe):
        """Add a new Recipe object to the list."""
        self._recipes.append(recipe)
        print("Added recipe:", recipe.get_name())

    def delete_recipe(self, name):
        """Delete a recipe by its name. Returns True if something was deleted."""
        for recipe in self._recipes:
            if recipe.get_name().lower() == name.lower():
                self._recipes.remove(recipe)
                print("Deleted recipe:", recipe.get_name())
                return True
        print("No recipe found with the name:", name)
        return False

    def edit_recipe(self, name, category, price, cooking_time, ingredients, calories):
        """
        Edit an existing recipe by name. The new values replace the old ones.
        Returns True if a recipe was edited.
        """
        for index, recipe in enumerate(self._recipes):
            if recipe.get_name().lower() == name.lower():
                # Build a new Recipe object with the updated values and
                # put it back in the same place in the list.
                updated = Recipe(name, category, price, cooking_time,
                                 ingredients, calories)
                self._recipes[index] = updated
                print("Edited recipe:", name)
                return True
        print("No recipe found with the name:", name)
        return False

    def search_by_name(self, name):
        """Return a list of recipes whose name contains the search text."""
        results = []
        for recipe in self._recipes:
            if name.lower() in recipe.get_name().lower():
                results.append(recipe)
        return results

    def search_by_category(self, category):
        """Return a list of recipes that belong to the given category."""
        results = []
        for recipe in self._recipes:
            if category.lower() == recipe.get_category().lower():
                results.append(recipe)
        return results

    def search_by_ingredient(self, ingredient):
        """Return a list of recipes that contain the given ingredient."""
        results = []
        for recipe in self._recipes:
            if ingredient.lower() in recipe.get_ingredients().lower():
                results.append(recipe)
        return results

    def show_recommended(self):
        """Print only the recipes where is_recommended() is True."""
        found = False
        for recipe in self._recipes:
            if recipe.is_recommended():
                recipe.show_short()
                found = True
        if not found:
            print("There are no recommended recipes right now.")

    def show_details(self, name):
        """Show full details of one recipe, like ordering a dish."""
        for recipe in self._recipes:
            if recipe.get_name().lower() == name.lower():
                print("\nYou selected this dish:")
                recipe.show_full()
                # Also show the logical breakdown for this recipe.
                logic = evaluate_recipe_logic(recipe)
                print("Logic -> P:", logic["P"], "Q:", logic["Q"],
                      "R:", logic["R"], "=> Recommended:", logic["Result"])
                return
        print("No recipe found with the name:", name)

    def sort_by_price(self):
        """Return the recipes sorted by price using the loop sort."""
        return self._loop_sorter.sort(self._recipes, "price")

    def sort_by_cooking_time(self):
        """Return the recipes sorted by cooking time using the recursive sort."""
        return self._recursive_sorter.sort(self._recipes, "cooking_time")
