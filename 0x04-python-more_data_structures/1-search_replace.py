#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # replaces all occurences of search with replace
    return ([elem if elm != search else replace for elem in my_list])
