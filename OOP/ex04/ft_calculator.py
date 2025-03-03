class calculator:
    """calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
            Calculate and print the dot product of two vectors.
        """
        product = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {product}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
            Add two vectors element-wise and print the result vector.
        """
        sum_list = [float(x) + float(y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {sum_list}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
            Subtract two vectors element-wise and print the result vector.
        """
        substract_list = [float(x) - float(y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is : {substract_list}")
