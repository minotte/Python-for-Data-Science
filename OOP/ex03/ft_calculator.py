class calculator:
    """Use it to make calcul"""
    def __init__(self, vector):
        """Init class calculator"""
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Add object at every number from the vector
        and print the result
        params:
            object : number
        """
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multipled object at every number from the vector
        and print the result
        params:
            object : number
        """
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Substract object at every number from the vector
        and print the result
        params:
            object : number
        """
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divided object at every number from the vector
        and print the result
        params:
            object : number
        Error:
            raise ValueError if object is 0
        """
        if object == 0:
            raise ValueError("Can't divide by 0")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
