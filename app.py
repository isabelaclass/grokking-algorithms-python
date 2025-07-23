import time
import json
from binary_search import binary_search
from linear_search import lienar_search


if __name__ == "__main__":

    with open('cities.json', 'r', encoding='utf_8') as file:
        cities = json.load(file)

    ordenaded_cities = sorted(city["nome"] for city in cities)

    item = "Paris"

    star_time_binary = time.perf_counter()
    result = binary_search(ordenaded_cities, item)
    end_time_binary = time.perf_counter()
    time_binary = (end_time_binary - star_time_binary) * 1000

    starr_time_linear = time.perf_counter()
    result_linear = lienar_search(ordenaded_cities, item)
    end_time_linear = time.perf_counter()
    time_linear = (end_time_linear - starr_time_linear) * 1000

    print(f"Binary Search Result: {result}, Time taken: {time_binary:.6f} ms")
    print(f"Linear Search Result: {result_linear}, Time taken: {time_linear:.6f} ms")