#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """
    A function that generates pascal triangle to given n rows

    args:
        n: number of rows to generate pascal triangle
    Return: A list of lists representing pascal triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
