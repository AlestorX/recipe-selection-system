# Intelligent Recipe Selection System

## Project description

This is a small Python console program. It keeps a list of recipes and helps
the user choose a good one. The user can show recipes, add new ones, delete,
edit, search, sort, and see "recommended" recipes.

A recipe is **recommended** when it is cheap, quick, and healthy at the same
time. The program also shows a truth table and compares two sorting algorithms.

The program uses only standard Python libraries: `csv`, `time`, and `abc`.
There are no extra installs needed.

## How to run

Open a terminal inside the project folder and type:

```
python main.py
```

If `python` does not work, try:

```
python3 main.py
```

## File structure

| File                | What it does                                              |
|---------------------|----------------------------------------------------------|
| `main.py`           | Shows the menu and runs the program loop.                |
| `recipe.py`         | The `Recipe` class (one recipe).                         |
| `recipe_manager.py` | The `RecipeManager` class (the list of recipes).         |
| `sorting.py`        | The two sorting algorithms.                              |
| `logic.py`          | The logical rule and the truth table.                    |
| `performance.py`    | The speed test for the two sorts.                        |
| `recipes.csv`       | The data file with all the recipes.                      |
| `README.md`         | This file.                                               |
| `PRESENTATION_NOTES.md` | Simple study notes for the presentation.             |

## Explanation of each class

- **Recipe** (`recipe.py`)
  Stores one recipe: name, category, price, cooking time, ingredients, and
  calories. It can print a short line or full details. It has four logical
  methods: `is_cheap()`, `is_quick()`, `is_healthy()`, and `is_recommended()`.

- **RecipeManager** (`recipe_manager.py`)
  Stores a list of `Recipe` objects. It loads and saves the CSV file, shows
  recipes, adds, deletes, edits, searches (by name, category, or ingredient),
  shows recommended recipes, and calls the sorting algorithms.

- **SortingAlgorithm** (`sorting.py`)
  An abstract class. It says every sorting algorithm must have a `sort` method.

- **LoopSort** (`sorting.py`)
  Sorts recipes using insertion sort (with loops).

- **RecursiveSort** (`sorting.py`)
  Sorts recipes using merge sort (with recursion).

## CSV dataset

The data is stored in `recipes.csv`. The first line is the header:

```
name,category,price,cooking_time,ingredients,calories
```

- `name` – the recipe name
- `category` – soup, starter, main dish, dessert, or breakfast
- `price` – a number like `8.5`
- `cooking_time` – minutes, a whole number
- `ingredients` – words separated by **spaces** (no commas, so the CSV stays valid)
- `calories` – a whole number

There are 12 recipes in the file.

## Sorting algorithms

The project uses two sorting algorithms written by hand. They do **not** use
Python's built-in `sorted()` or `list.sort()`.

- **LoopSort = insertion sort.** It takes one recipe at a time and moves it left
  until it is in the right place. Speed: **O(n^2)**.
- **RecursiveSort = merge sort.** It splits the list in half again and again,
  then merges the small sorted lists back together. Speed: **O(n log n)**.

Both can sort by **price** or by **cooking time**. If two recipes have the same
value, the recommended one comes first.

## Logical variables and truth table

The program uses three logical variables:

- **P = cheap** → price is 10 or less
- **Q = quick** → cooking time is 30 minutes or less
- **R = healthy** → calories are 500 or less

The rule for a recommended recipe is:

```
P AND Q AND R
```

This is only `True` when all three are `True`. The truth table shows all 8
combinations of `P`, `Q`, and `R` and the final result.

## Performance analysis

Menu option 14 runs a small speed test. It sorts copies of the recipe list with
both algorithms and measures the time with `time.perf_counter()`. Then it prints
the Big-O explanation:

- Insertion sort is O(n^2)
- Merge sort is O(n log n)

## Error handling

The program tries not to crash:

- A wrong menu choice shows a friendly message.
- Typing text instead of a number asks again.
- If `recipes.csv` is missing, it starts with an empty list and shows a message.
- If one CSV row has wrong data, that row is skipped.
- If a search finds nothing, it shows "No recipes matched your search."

## Future improvements

- Let the user sort by other things, like calories.
- Add more recipes to the CSV file.
- Save recipes automatically after every change.
- Add a simple search that matches more than one ingredient at a time.
- Add a small graphical interface later.
