from brand import Brand
from application import EventApplication

#vytvořim si slovník pro možnosti místností
ROOM_CHOICES = {
    1: "Hallway",
    2: "Main Hall",
    3: "Side Hall"
}
#spuštění hlavní aplikace
def main():
    event_application = EventApplication()

    while True:
        print("\nWelcome to our system. What can we help you with?")
        print("1. Sign-up a brand for the event")
        print("2. Display all signed-up brands")
        print("3. Search signed-up brand")
        print("4. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            brand_name = input("Brand name: ")
            contact_person_name = input("Contact Person: ")
            email = input("Email: ")
            phone_number = input("Phone number: ")


            print("Room Choice:")
            for number, room_name in ROOM_CHOICES.items():
                print(f"{number}. {room_name}")
            room_choice = input("Enter preferred room choice number: ")
            if not room_choice.isdigit() or int(room_choice) not in ROOM_CHOICES:
                print("We don't have this room. Please enter 1,2 or 3.")
                continue

            preferred_room_choice = ROOM_CHOICES[int(room_choice)]

            if not brand_name:
                print("Brand name cannot be empty. Please try again.")
                continue

            brand = Brand(brand_name, contact_person_name, email, phone_number, preferred_room_choice)
            event_application.add_brand(brand)
            print("Brand added successfully.")

        elif choice == "2":
            print("\nList of signed up brands:")
            event_application.display_all_brands()

        elif choice == "3":
            brand_name = input("Enter brand name: ")
            found_brand = event_application.search_brand(brand_name)

            if found_brand:
                print("\nThis is the brand you were looking for:")
                print(found_brand)
            else:
                print("Brand not found.")

        elif choice == "4":
            print("Thank you for using our service. Have a great day!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
