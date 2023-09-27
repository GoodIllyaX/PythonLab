class Restaurant:
    def __init__(self, restaurant_type, name):
        self.restaurant_type = restaurant_type
        self.name = name

    def prepare_food(self, item):
        print(f"{self.name} is taking an order on {item}.")

    def take_order(self, item):
        print(f"- is preparing {item}.")

    def serve_food(self, item):
        print(f"- is serving {item}.")

class SushiRestaurant(Restaurant):
    def __init__(self, name):
        super().__init__("Sushi", name) #тип и назва

    def menu(self):
        print(f"{self.name}\n Menu:\n")
        print("1. Salmon Sushi")
        print("2. Sushi Roll")

class Pizzeria(Restaurant):
    def __init__(self, name):
        super().__init__("Pizza", name)

    def menu(self):
        print(f"{self.name}\n Menu:\n")
        print("1. Pepperoni Pizza")
        print("2. Margherita Pizza")

class SteakHouse(Restaurant):
    def __init__(self, name):
        super().__init__("Steak", name)

    def menu(self):
        print(f"{self.name}\n Menu:\n")
        print("1. Ribeye Steak")
        print("2. Filet Mignon Steak")



choice = input("Choose a restaurant (1. Sushi Restaurant, 2. Pizzeria, 3. SteakHouse): ")
choice = int(choice)

if choice == 1:
    restaurant = SushiRestaurant("\nSushi Delight")
    restaurant.menu()
    sub_choice = input("Enter your choice (1 or 2): ")
    if sub_choice == '1':
        restaurant.prepare_food("Salmon Sushi") #item
        restaurant.take_order("Salmon Sushi")
        restaurant.serve_food("Salmon Sushi")
    elif sub_choice == '2':
        restaurant.prepare_food("Sushi Roll")
        restaurant.take_order("Sushi Roll")
        restaurant.serve_food("Sushi Roll")
    else:
        print("Invalid choice. ")

elif choice == 2:
    restaurant = Pizzeria("\nPizza Haven")
    restaurant.menu()
    sub_choice = input("Enter your choice (1 or 2): ")
    if sub_choice == '1':
        restaurant.prepare_food("Pepperoni Pizza")
        restaurant.take_order("Pepperoni Pizza")
        restaurant.serve_food("Pepperoni Pizza")
    elif sub_choice == '2':
        restaurant.prepare_food("Margherita Pizza")
        restaurant.take_order("Margherita Pizza")
        restaurant.serve_food("Margherita Pizza")
    else:
        print("Invalid choice. ")

elif choice == 3:
    restaurant = SteakHouse("\nThe Meaty Grill")
    restaurant.menu()
    sub_choice = input("Enter your choice (1 or 2): ")
    if sub_choice == '1':
        restaurant.prepare_food("Ribeye Steak")
        restaurant.take_order("Ribeye Steak")
        restaurant.serve_food("Ribeye Steak")
    elif sub_choice == '2':
        restaurant.prepare_food("Filet Mignon Steak")
        restaurant.take_order("Filet Mignon Steak")
        restaurant.serve_food("Filet Mignon Steak")
    else:
        print("Invalid sub-choice.")
else:
    print("Invalid choice. ")
