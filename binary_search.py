def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

def binary_search_cities(cities, city):
    names = [city.name for city in cities]
    index = binary_search(names, city.name) 
    return index