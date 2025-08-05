from Models.Hotel import Hotel, sum_price_hotels, find_max_price_recursive

class City:
    def __init__(self, name):
        self.name = name
        self.hotels_head = None

    def add_hotel(self, name, location, rating, price_per_night):
        new_hotel = Hotel(name, location, rating, price_per_night)
        if not self.hotels_head:
            self.hotels_head = new_hotel
        else:
            current = self.hotels_head
            while current.next:
                current = current.next
            current.next = new_hotel
    
    def list_hotels(self):
        if not self.hotels_head:
            print(f"No hotels found in {self.name}.")
            return
        
        current = self.hotels_head
        while current:
            print(f"Hotel Name: {current.name}, Location: {current.location}, Rating: {current.rating}, Price per Night: ${current.price_per_night}")
            current = current.next
    
    def return_hotels_array(self):
        hotels = []
        current = self.hotels_head
        while current:
            hotels.append({
                "name": current.name,
                "location": current.location,
                "rating": current.rating,
                "price_per_night": current.price_per_night
            })
            current = current.next
        return hotels
    
    def sum_prices(self):
        return sum_price_hotels(self.hotels_head)
    
    def get_max_price(self):
        return find_max_price_recursive(self.hotels_head)