from S1E9 import Character


class Baratheon(Character):
    """Baratheon, child of Charater."""

    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character with name and alive status."""
        super().__init__(first_name, is_alive)

    def __str__(self):
        """Return a readable string representation of the character."""
        return f"{self.first_name} {self.family_name}: \
                (Eyes: {self.eyes}, Hair: {self.hairs})"

    def __repr__(self):
        """Return a technical representation of the character."""
        return f"Baratheon(first_name='{self.first_name}', \
                is_alive={self.is_alive})"


class Lannister(Character):
    """Lannister, child of Charater."""

    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)

    def __str__(self):
        """Return a readable string representation of the character."""
        return f"{self.first_name} {self.family_name}: \
                (Eyes: {self.eyes}, Hair: {self.hairs})"

    def __repr__(self):
        """Return a technical representation of the character."""
        return f"Lannister(first_name='{self.first_name}', \
                is_alive={self.is_alive})"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister instance."""
        return cls(first_name, is_alive)
