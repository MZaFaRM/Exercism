"""Leap year check"""

def leap_year(year):
    """
        Determines if a given year is a leap year.

        Args:
            year (int): The year to be checked.

        Returns:
            bool: True if the year is a leap year, False otherwise.

        Example:
            ```python
            year = 2020
            is_leap = leap_year(year)
            print(is_leap)  # Output: True
            ```
    """
    return year % 400 == 0 if year % 100 == 0 else year % 4 == 0
        
