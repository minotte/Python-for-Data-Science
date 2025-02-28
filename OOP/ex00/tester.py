from S1E9 import Character, Stark

try:
    # Test with Ned Stark
    Ned = Stark("Ned")
    print(Ned.__dict__)  # {'first_name': 'Ned', 'is_alive': True}
    print(Ned.is_alive)  # True
    Ned.die()
    print(Ned.is_alive)  # False

    # Print docstrings
    print(Ned.__doc__)       # "Class representing a member of House Stark..."
    print(Ned.__init__.__doc__)  # "Initialize a character..."
    print(Ned.die.__doc__)    # "Set is_alive attribute to False..."

    print("---")

    # Test with Lyanna Stark
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)  # {'first_name': 'Lyanna', 'is_alive': False}

    # Test that Character cannot be instantiated
    hodor = Character("Hodor")
except TypeError as e:
    print(f"TypeError: {e}")  # Expected TypeError
