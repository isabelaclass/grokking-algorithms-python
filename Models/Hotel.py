
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
