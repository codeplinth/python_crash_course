def make_pizza(size,*toppings):
    """Summarize the list of toppings in the pizza"""
    print(f"\nMake a {size} inch pizza with the following toppings")
    for t in toppings:
        print(f"- {t}")
    
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
