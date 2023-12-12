#definuji si třídu pro přihlášené značky a informace, které od nich chci získat
class Brand:
    def __init__(self, brand_name, contact_person_name, email, phone_number, preferred_room_choice):
        self.brand_name = brand_name
        self.contact_person_name = contact_person_name
        self.email = email
        self.phone_number = phone_number
        self.preferred_room_choice = preferred_room_choice

    def __str__(self):
        return f"Brand Name: {self.brand_name}, Contact Person: {self.contact_person_name}, " \
               f"Email: {self.email}, Phone Number: {self.phone_number}, Preferred Room Choice: {self.preferred_room_choice}"
