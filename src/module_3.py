class Calculator:
    """
    The Calculator class provides basic arithmetic operations.

    The purpose of this class is to serve as a simple calculator
    implementation for use in CI/CD testing. The 'add' method has
    been intentionally implemented with a bug to demonstrate
    how a failing test can be used to validate the CI/CD pipeline.
    """

    def add(self, a, b):
        """
        Adds two numbers together, but with a bug.

        This method is intentionally implemented with a bug to
        demonstrate how a failing test can be used to validate
        the CI/CD pipeline. The bug is that the method always
        returns the value of 'a' instead of the correct sum.

        Args:
            a (int or float): The first number to add.
            b (int or float): The second number to add.

        Returns:
            int or float: The value of 'a' instead of the correct sum.
        """
        return a

    def subtract(self, a, b):
        """
        Subtracts two numbers.

        Args:
            a (int or float): The number to subtract from.
            b (int or float): The number to subtract.

        Returns:
            int or float: The result of subtracting 'b' from 'a'.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Args:
            a (int or float): The first number to multiply.
            b (int or float): The second number to multiply.

        Returns:
            int or float: The result of multiplying 'a' and 'b'.
        """
        return a * b

    def divide(self, a, b):
        """
        Divides two numbers.

        Args:
            a (int or float): The number to divide.
            b (int or float): The number to divide by.

        Returns:
            int or float: The result of dividing 'a' by 'b'.
        """
        return a / b