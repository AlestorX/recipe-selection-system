from abc import ABC, abstractmethod

#########################################################################
class SortingAlgorithm(ABC):
    """Abstract base class. Every sorting algorithm must have a sort method."""

    @abstractmethod
    def sort(self, recipes, key):
        """Sort and return a list of recipes by the given key."""
        pass
 ############################################################################
    def get_value(self, recipe, key):
        """Helper: read the primary value (price or cooking_time) of a recipe."""
        if key == "price":
            return recipe.get_price()
        else:
            return recipe.get_cooking_time()

    def comes_first(self, a, b, key):
        """
        Return True if recipe a should come before recipe b.

        Primary sort: the chosen key (price or cooking_time), smaller first.
        Secondary sort: if the primary values are equal, a recommended recipe
        comes before a non-recommended one.
        """
        value_a = self.get_value(a, key)
        value_b = self.get_value(b, key)
        if value_a != value_b:
            return value_a < value_b
        # Primary values are equal -> use is_recommended() as the tie breaker.
        # True counts as 1 and False as 0, so recommended (True) wins.
        return a.is_recommended() and not b.is_recommended()

#########################################################################
class LoopSort(SortingAlgorithm):
    """Insertion sort built with simple loops."""

    def sort(self, recipes, key):
        # Work on a copy so we do not change the original list.
        items = list(recipes)
        # Insertion sort: take each item and move it left into place.
        for i in range(1, len(items)):
            current = items[i]
            j = i - 1
            # Move bigger items one step to the right.
            while j >= 0 and self.comes_first(current, items[j], key):
                items[j + 1] = items[j]
                j = j - 1
            items[j + 1] = current
        return items


class RecursiveSort(SortingAlgorithm):
    """Merge sort built with recursion."""

    def sort(self, recipes, key):
        items = list(recipes)
        # Base case: a list of 0 or 1 items is already sorted.
        if len(items) <= 1:
            return items
        # Split the list into two halves.
        middle = len(items) // 2
        left = self.sort(items[:middle], key)   # recursive call
        right = self.sort(items[middle:], key)  # recursive call
        # Merge the two sorted halves back together.
        return self._merge(left, right, key)

    def _merge(self, left, right, key):
        """Merge two sorted lists into one sorted list."""
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if self.comes_first(left[i], right[j], key):
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        # Add whatever is left over from either side.
        result.extend(left[i:])
        result.extend(right[j:])
        return result
 ##########################################################################