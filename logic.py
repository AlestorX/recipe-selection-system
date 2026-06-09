def explain_logic():
    """Print a short explanation of the logical rule used in the project."""
    print("\nP = cheap: price <= 10")
    print("Q = quick: cooking time <= 30")
    print("R = healthy: calories <= 500")
    print("Recommended = P AND Q AND R")


def show_truth_table():
    """Print a compact truth table for P AND Q AND R (1 = True, 0 = False)."""
    print("\nTruth table: P AND Q AND R")
    print("P Q R | Result")
    # Loop over every combination of True/False for P, Q and R.
    for p in [0, 1]:
        for q in [0, 1]:
            for r in [0, 1]:
                result = p and q and r
                print(p, q, r, "|", result)


def evaluate_recipe_logic(recipe):
    """
    Work out the logical values (P, Q, R and the result) for one recipe
    and return them as a dictionary. This lets other code reuse the rule.
    """
    p = recipe.is_cheap()
    q = recipe.is_quick()
    r = recipe.is_healthy()
    result = p and q and r
    return {"P": p, "Q": q, "R": r, "Result": result}
