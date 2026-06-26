from recipe import Recipe
from recipe_manager import RecipeManager
from logic import explain_logic, show_truth_table
from performance import run_performance_analysis


# ---------------------------------------------------------------------------
# Small helper functions for safe input
# ---------------------------------------------------------------------------
##################################################################
def ask_float(message):
    """Ask the user for a number with a decimal point. Repeat until valid."""
    while True:
        text = input(message)
        try:
            return float(text)
        except ValueError:
            print("Please enter a valid number, for example 8.5")


def ask_int(message):
    """Ask the user for a whole number. Repeat until valid."""
    while True:
        text = input(message)
        try:
            return int(text)
        except ValueError:
            print("Please enter a valid whole number, for example 30")
##################################################################


def show_list(recipes):
    """Print every recipe in a list as a short one-line summary."""
    print("(* means the recipe is recommended)")
    for recipe in recipes:
        recipe.show_short()


def print_results(results):
    """Print a list of recipes from a search, or a friendly message."""
    if results:
        for recipe in results:
            recipe.show_short()
    else:
        print("No recipes matched your search.")


# ---------------------------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------------------------
def show_menu():
    """Print the main menu options, grouped into clear sections."""
    print("\n===== Intelligent Recipe Selection System =====")
    print("\nRecipe Menu:")
    print("1. Show all recipes")
    print("2. View recipe details")
    print("3. Add recipe")
    print("4. Delete recipe")
    print("5. Edit recipe")
    print("\nSearch Menu:")
    print("6. Search by name")
    print("7. Search by category")
    print("8. Search by ingredient")
    print("\nSorting and Recommendation:")
    print("9. Sort by price")
    print("10. Sort by cooking time")
    print("11. Show recommended recipes")
    print("\nExtra Tools:")
    print("12. Show how recommendations work")
    print("13. Show the truth table")
    print("14. Compare sorting speed")
    print("\n15. Save recipes")
    print("0. Exit")

 ##################################################################################
def main():
    """The main program loop."""
    manager = RecipeManager()
    manager.load_recipes()  # load recipes when the program starts

    while True:
        show_menu()
        try:
            choice = input("Choose an option: ").strip()
        except EOFError:
            # Happens if input ends (for example Ctrl+D). Save and exit nicely.
            print("\nInput ended. Saving and exiting.")
            manager.save_recipes()
            break

        if choice == "1":
            manager.show_all()

        elif choice == "2":
            name = input("Enter the recipe name: ").strip()
            manager.show_details(name)

        elif choice == "3":
            # Collect the details for a new recipe with safe input.
            name = input("Name: ").strip()
            category = input("Category (soup/starter/main dish/dessert/breakfast): ").strip()
            price = ask_float("Price (for example 8.5): ")
            cooking_time = ask_int("Cooking time in minutes: ")
            ingredients = input("Ingredients (separated by spaces): ").strip()
            calories = ask_int("Calories: ")
            new_recipe = Recipe(name, category, price, cooking_time, ingredients, calories)
            manager.add_recipe(new_recipe)

        elif choice == "4":
            name = input("Enter the recipe name to delete: ").strip()
            manager.delete_recipe(name)

        elif choice == "5":
            # Edit an existing recipe by entering new values.
            name = input("Enter the recipe name to edit: ").strip()
            category = input("New category: ").strip()
            price = ask_float("New price (for example 8.5): ")
            cooking_time = ask_int("New cooking time in minutes: ")
            ingredients = input("New ingredients (separated by spaces): ").strip()
            calories = ask_int("New calories: ")
            manager.edit_recipe(name, category, price, cooking_time, ingredients, calories)

        elif choice == "6":
            name = input("Enter a name to search for: ").strip()
            print_results(manager.search_by_name(name))

        elif choice == "7":
            category = input("Enter a category to search for: ").strip()
            print_results(manager.search_by_category(category))

        elif choice == "8":
            ingredient = input("Enter an ingredient to search for: ").strip()
            print_results(manager.search_by_ingredient(ingredient))

        elif choice == "9":
            # Sort by price using the loop sort (insertion sort).
            sorted_list = manager.sort_by_price()
            print("\nRecipes sorted by price (loop sort):")
            show_list(sorted_list)

        elif choice == "10":
            # Sort by cooking time using the recursive sort (merge sort).
            sorted_list = manager.sort_by_cooking_time()
            print("\nRecipes sorted by cooking time (recursive sort):")
            show_list(sorted_list)

        elif choice == "11":
            print("\nRecommended recipes:")
            manager.show_recommended()

        elif choice == "12":
            explain_logic()

        elif choice == "13":
            show_truth_table()

        elif choice == "14":
            run_performance_analysis(manager.get_recipes())

        elif choice == "15":
            manager.save_recipes()

        elif choice == "0":
            manager.save_recipes()
            print("Goodbye!")
            break

        else:
            # Any other input is invalid, but we do not crash.
            print("Invalid choice. Please enter a number from the menu.")


# This makes sure main() only runs when we start the file directly.
if __name__ == "__main__":
    main()
