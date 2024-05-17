import numpy as np


def _slope_and_intercept(x, y):
    """
    Calculate the slope and intercept of a line for the given set of x and y data points.

    Parameters
    ------
    x : array-like :The x-coordinates of the data points.
    y : array-like :The y-coordinates of the data points.

    Returns
    ------
    tuple : A tuple containing the slope and intercept of the line.

    Raises
    ------
    ValueError : If the lists of x and y values do not have the same number of elements or if all x values are the same.

    Examples
    ------
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> _slope_and_intercept(x, y)
    (2.0, 0.0)
    """
    # Check if the lists of x and y values have the same number of elements
    if len(x) != len(y):
        return "The lists of x and y values must have the same number of elements."

    # Calculate the mean (average) of the x values and the y values
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the numerator of the slope formula
    numerator = sum((yi - mean_y) * (xi - mean_x) for xi, yi in zip(x, y))
    # Calculate the denominator of the slope formula
    denominator = sum((xi - mean_x) ** 2 for xi in x)

    # Check if the denominator is zero (which would make the slope undefined)
    if denominator == 0:
        return "The denominator is zero, which means all x values are the same. Slope is undefined."

    # Calculate the slope (m)
    slope = numerator / denominator
    # Calculate the intercept (c)
    intercept = mean_y - slope * mean_x

    # Return both the slope and intercept
    return slope, intercept


def linear_equation(x, y):
    """
    Construct the linear equation in the form of y = mx + c and provide the slope and intercept.

    Parameters
    ------
    x : array-like: The x-coordinates of the data points.
    y : array-like: y-coordinates of the data points.

    Returns
    ------
    str: A string representation of the linear equation and the values of the slope and intercept.

    Notes
    ------
    This function calls the `_slope_and_intercept` function to calculate the slope and intercept.
    It then constructs a string that represents the linear equation.
    If the intercept is zero, the equation is simplified to y = mx.

    Examples
    ------
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 4, 6, 8, 10]
    >>> print(linear_equation(x, y))
     linear equation
    -----------------
     y = 2.0x
    -----------------
     slope = 2.0
     intercept = 0.0
    """
    slope = _slope_and_intercept(x, y)[0]
    intercept = _slope_and_intercept(x, y)[1]

    if intercept != 0:
        return f" linear equation\n-----------------\n y = {slope}x + {intercept}\n-----------------\n" \
               f" slope = {slope}\n intercept = {intercept}"
    else:
        return f" linear equation\n-----------------\n y = {slope}x\n-----------------\n" \
               f" slope = {slope}\n intercept = {intercept}"
