class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


class Bangladesh_bus_system:
    def __init__(self):
        self.system = BusSystem()
        self.admin = Admin("admin", "1234")
        self.current_user = None
        self.fare = 500

    def add_bus(self, number, route, seats):
        if self.current_user != "admin":
            print("Admin Login Is Required!")
            return False
            
        new_bus = Bus(number, route, seats)
        self.system.buses.append(new_bus)
        print(f"Bus {number} added Successfully..")
        return True

    def find_bus(self, bus_number):
        for bus in self.system.buses:
            if bus.number == bus_number:
                return bus
        return None

    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if not bus:
            print("Bus not found...")
            return False
            
        if bus.available_seats() <= 0:
            print("No available seats on this bus...")
            return False
            
        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.system.passengers.append(passenger)
            print(f"Ticket booked successfully \U0001F600 Fare: {self.fare} Tk")
            print(f"Passenger: {name} , Bus: {bus_number} , Route: {bus.route}")
            return True
        return False

    def show_buses(self):
        if not self.system.buses:
            print("No buses available 😭")
            return
            
        print("\nAvailable Buses: ")
        print("No.\tRoute\t\tAvailable Seats")
        for bus in self.system.buses:
            print(f"{bus.number}\t{bus.route}\t\t{bus.available_seats()}")

    def admin_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if self.admin.login(username, password):
            self.current_user = "admin"
            print("Admin login successful 🌸")
            return True
        else:
            print("Invalid credentials❌")
            return False

    def admin_logout(self):
        self.current_user = None
        print("Logged out successfully 👍")

    def user_menu(self):
        while True:
            print("\n===== Bangladesh Bus Ticket Booking System =====")
            print("1. Admin Login")
            print("2. Book Ticket")
            print("3. View Buses")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                if self.admin_login():
                    self.admin_menu()
                    
            elif choice == "2":
                bus_number = input("Enter bus number: ")
                name = input("Enter passenger name: ")
                phone = input("Enter passenger phone: ")
                self.book_ticket(bus_number, name, phone)
                
            elif choice == "3":
                self.show_buses()
                
            elif choice == "4":
                print("Thank you for using our system ❤️")
                break
                
            else:
                print("Invalid choice! Please try again.")

    def admin_menu(self):
        while self.current_user == "admin":
            print("\n===== Admin Menu =====")
            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Logout")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                number = input("Enter bus number: ")
                route = input("Enter bus route: ")
                try:
                    seats = int(input("Enter total seats: "))
                    self.add_bus(number, route, seats)
                except ValueError:
                    print("Invalid seat number!")
                    
            elif choice == "2":
                self.show_buses()
                
            elif choice == "3":
                self.admin_logout()
                
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    bus_system = Bangladesh_bus_system()
    bus_system.user_menu()