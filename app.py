import time
import json
from Models.City import City
from Models.Hotel import sort_selection_hotel_price
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
        hotel_array = city_found.return_hotels_array()
        print(f"\nHotels array: {hotel_array}")
        sorted_hotels = sort_selection_hotel_price(hotel_array)
        print("\nSorted hotels by price:")
        for hotel in sorted_hotels:
            print(f"- {hotel['name']} ({hotel['location']}) - {hotel['rating']}★ - R$ {hotel['price_per_night']}/night")
    else:
        print(f"\nCity '{item}' not found.")