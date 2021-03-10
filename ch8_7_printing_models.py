#modifying a list in a function
def print_models(unprinted_designs,completed_models):
    """
    Simulate printing designs until none are left.
    Move each design to completed models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show completed models that were printed"""
    print("\nThe following models have been printed")
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
