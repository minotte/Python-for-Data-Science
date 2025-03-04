import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random ID consisting of 15 lowercase letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A dataclass representing a student with a name, surname, active status,
    auto-generated login, and a unique random ID.
    """
    name: str
    surname: str
    activate: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """
        Automatically generate the login after initialization.
        The login is the first letter in capital of the name concatenated
        with the surname in lowercase.
        """
        self.login = self.name[0].capitalize() + self.surname.lower()
