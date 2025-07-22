def lienar_search(list, item):
    for index, element in enumerate(list):
        if element == item:
            return index
    return None