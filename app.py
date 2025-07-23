import time
import json
from Models.City import City
from binary_search import binary_search
from linear_search import lienar_search


if __name__ == "__main__":

    with open('cities.json', 'r', encoding='utf_8') as file:
        cities = json.load(file)

    ordenaded_cities = sorted(city["nome"] for city in cities)
    ordenaded_cities_objects = [City(name) for name in ordenaded_cities]

    item = "Paris"

    result = binary_search(ordenaded_cities, item)

    if result is not None:
        city_found = ordenaded_cities_objects[result]
        city_found.add_hotel("Hotel Tour Eiffel", "Paris, França", 5, 1200)
        city_found.add_hotel("Hotel Budget Paris", "Paris, França", 3, 450)

        print(f"\nHotels in {city_found.name}:")
        city_found.list_hotels()
    else:
        print(f"\nCity '{item}' not found.")