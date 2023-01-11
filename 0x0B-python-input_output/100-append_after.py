#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 19:42:07 2023
@author: Cinnamon Okwandu
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line after each line containing a specific string
    Arguments:
        filename (str): The name of the file
        search_string (str): The string to math
        new_string (str): The string to insert after matching
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as file:
        content = "".join(lines)
        file.write(content)
