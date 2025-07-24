
class Hotel:
    def __init__(self, name, location, rating, price_per_night):
        self.name = name
        self.location = location
        self.rating = rating
        self.price_per_night = price_per_night
        self.next = None

    def add_hotel(self, name, location, rating, price_per_night):
        new_hotel = Hotel(name, location, rating, price_per_night)
        if not self.hotels_head:
            self.hotels_head = new_hotel
        else:
            current = self.hotels_head
            while current.next:
                current = current.next
            current.next = new_hotel

def sort_selection_hotel_price(hotels):
    n = len(hotels)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if hotels[j]["price_per_night"] < hotels[min_idx]["price_per_night"]:
                min_idx = j
        if min_idx != i:
            hotels[i], hotels[min_idx] = hotels[min_idx], hotels[i]
    return hotels
