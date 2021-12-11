import requests
from restaurant.models import restaurant

class fetch():
    def fill_data(self, n):
        for _ in range(n):
            data = requests.get(url='https://random-data-api.com/api/restaurant/random_restaurant')
            data = data.json()
            _restaurant = restaurant()
            _restaurant.name = data['name']
            _restaurant.type = data['type']
            _restaurant.description = data['description']
            _restaurant.save()

    def run(self):
        self.fill_data(20)
