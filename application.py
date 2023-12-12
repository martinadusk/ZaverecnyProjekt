from brand import Brand

#definuji třídu pro správu dat
class EventApplication:
    def __init__(self):
        self.brands = []

#přidávám značku
    def add_brand(self, brand):
        self.brands.append(brand)

#zobrazuji všechny značky
    def display_all_brands(self):
        for brand in self.brands:
            print(brand)

#vyhledávám značky
    def search_brand(self, brand_name):
        for brand in self.brands:
            if brand.brand_name.lower() == brand_name.lower():
                return brand
        return None
