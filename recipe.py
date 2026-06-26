class Recipe:
    """One recipe with all of its information."""

    def __init__(self, name, category, price, cooking_time, ingredients, calories):
        # We use a leading underscore to show these attributes are "private"
        # (encapsulation). Other code should use the methods below instead of
        # touching the attributes directly.
        self._name = name
        self._category = category
        self._price = float(price)
        self._cooking_time = int(cooking_time)
        self._ingredients = ingredients
        self._calories = int(calories)

    # --- Simple getters so other classes can read the values safely ---
    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_price(self):
        return self._price

    def get_cooking_time(self):
        return self._cooking_time

    def get_ingredients(self):
        return self._ingredients

    def get_calories(self):
        return self._calories

    # --- Logical methods (used in the logic rule and the truth table) ---
    ######################################################################
    def is_cheap(self):
        """P = cheap: price is 10 or less."""
        return self._price <= 10

    def is_quick(self):
        """Q = quick: cooking time is 30 minutes or less."""
        return self._cooking_time <= 30

    def is_healthy(self):
        """R = healthy: calories are 500 or less."""
        return self._calories <= 500

    def is_recommended(self):
        """A recipe is recommended only when cheap AND quick AND healthy."""
        return self.is_cheap() and self.is_quick() and self.is_healthy()
 ########################################################################
    # --- Display methods ---
    def show_short(self):
        """Print a short one-line summary of the recipe."""
        star = "*" if self.is_recommended() else " "
        print("{} {:<20} | {:<10} | ${:<6} | {:>3} min | {:>4} cal".format(
            star,
            self._name,
            self._category,
            self._price,
            self._cooking_time,
            self._calories,
        ))

    def show_full(self):
        """Print all of the details of the recipe."""
        print("-" * 40)
        print("Name        :", self._name)
        print("Category    :", self._category)
        print("Price       : $" + str(self._price))
        print("Cooking time:", self._cooking_time, "minutes")
        print("Ingredients :", self._ingredients)
        print("Calories    :", self._calories)
        print("Recommended :", "Yes" if self.is_recommended() else "No")
        print("-" * 40)

    def to_row(self):
        """Turn the recipe back into a list for saving to the CSV file."""
        return [
            self._name,
            self._category,
            self._price,
            self._cooking_time,
            self._ingredients,
            self._calories,
        ]
