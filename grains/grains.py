"""
The servant told the king :
    "I would like to have grains of wheat. 
    One grain on the first square of a 
    chess board, with the number of grains 
    doubling on each successive square."
"""


def square(number):
    """
        Calculates the number of grains in a given square.

        Args:
            number (int): The number of square..

        Returns:
            int: The number of grains in that square.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 1 << (number - 1)


def total():
    """
        Calculates the total number of grains on the board.

        Args:
            None

        Returns:
            int: The total number of grains on the board.
    """
    return (1 << 64) - 1
