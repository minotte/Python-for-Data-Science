from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Create a monster?"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)
        self.family_name = Baratheon.family_name
        self.eyes = Baratheon.eyes
        self.hairs = Baratheon.hairs

    def set_eyes(self, color: str):
        """Set eyes color."""
        self.eyes = color

    def set_hairs(self, color: str):
        """Set hairs color."""
        self.hairs = color

    def get_eyes(self) -> str:
        """Get eyes color."""
        return (self.eyes)

    def get_hairs(self) -> str:
        """Get hairs color."""
        return (self.hairs)
