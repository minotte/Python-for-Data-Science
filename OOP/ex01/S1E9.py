from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class Character"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor
        Parameters:
            - firsname(str)
            - is_alive (bool, optional): by default is True
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to change the health state of the character."""
        self.is_alive = False


class Stark(Character):
    """Stark, child of Charater."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with name and alive status."""
        super().__init__(first_name, is_alive)

    def die(self):
        """call the Method die from parent"""
        super().__init__(self)
