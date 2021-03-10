#function with default parameter
def describe_pet(pet_name,animal_type='dog'): 
    """Displays information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

#a dog named willie
describe_pet('willie')

#a hamster named harry
describe_pet('harry','hamster') #positional arguments
describe_pet(animal_type='hamster',pet_name='harry') #key word arguments
describe_pet(pet_name='harry',animal_type='hamster')

