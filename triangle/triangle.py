"""Checks if the triangle is equilateral isosceles or scalene"""


def equilateral(sides):
    """
    Determines if a triangle with the given side lengths is equilateral.

    Args:
        sides (list): A list of three side lengths of the triangle.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.

    Example:
        ```python
        sides = [5, 5, 5]
        is_equilateral = equilateral(sides)
        print(is_equilateral)  # Output: True
        ```
    """
    return is_triangle(sides) and (len(set(sides)) == 1) and (sum(sides) != 0)


def isosceles(sides):
    """
    Determines if a triangle with the given side lengths is isosceles.

    Args:
        sides (list): A list of three side lengths of the triangle.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.

    Example:
        ```python
        sides = [5, 5, 6]
        is_isosceles = isosceles(sides)
        print(is_isosceles)  # Output: True
        ```
    """

    return is_triangle(sides) and (len(set(sides)) <= 2) and (sum(sides) != 0)


def scalene(sides):
    """
    Determines if a triangle with the given side lengths is scalene.

    Args:
        sides (list): A list of three side lengths of the triangle.

    Returns:
        int: The number of unique side lengths in the triangle.

    Example:
        ```python
        sides = [3, 4, 5]
        num_unique_sides = scalene(sides)
        print(num_unique_sides)  # Output: 3
        ```
    """
    return is_triangle(sides) and (len(set(sides)) == 3) and (sum(sides) != 0)


def is_triangle(sides):
    """
        Determines if the given side lengths can form a valid triangle.

        Args:
            sides (list): A list of three side lengths of the triangle.

        Returns:
            bool: True if the side lengths can form a triangle, False otherwise.

        Example:
            ```python
            sides = [3, 4, 5]
            is_triangle = is_triangle(sides)
            print(is_triangle)  # Output: True
            ```
    """
    a, b, c = sides
    return a + b >= c and b + c >= a and a + c >= b
