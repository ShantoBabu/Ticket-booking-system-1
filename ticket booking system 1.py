# Bus Ticket Booking System with Ticket Rent and Memo

class Bus:
    def __init__(self, bus_number, destination, departure_time, total_seats, ticket_price):
        self.bus_number = bus_number
        self.destination = destination
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_users = []

    def display_details(self):
        print(f"Bus Number: {self.bus_number}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Ticket Price: {self.ticket_price}Tk per seat")
        print(f"Available Seats: {self.available_seats}\n")

    def book_ticket(self, user_name, seats_to_book):
        if self.available_seats >= seats_to_book:
            self.available_seats -= seats_to_book
            total_cost = seats_to_book * self.ticket_price
            self.booked_users.append((user_name, seats_to_book, total_cost))
            print(f"\nBooking successful! {seats_to_book} seat(s) booked for {user_name}.")
            print(f"Total Rent: {total_cost}Tk")
            self.generate_memo(user_name, seats_to_book, total_cost)
        else:
            print("Sorry, not enough seats available.")

    def display_bookings(self):
        if len(self.booked_users) == 0:
            print("No bookings yet.")
        else:
            print("Booking Details:")
            for user, seats, cost in self.booked_users:
                print(f"Name: {user}, Seats: {seats}, Total Rent: {cost}")

    def generate_memo(self, user_name, seats_to_book, total_cost):
        print("\n--- Booking Memo (Receipt) ---")
        print(f"Passenger Name: {user_name}")
        print(f"Bus Number: {self.bus_number}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Seats Booked: {seats_to_book}")
        print(f"Total Rent: {total_cost}Tk")
        print("-----------------------------\n")


def main():
    # List of buses
    buses = [
        Bus("101", "Dhaka", "10:00 AM", 40, 700),  # 700 per seat
        Bus("102", "Chittagong", "12:00 PM", 50, 900),   # 900 per seat
        Bus("103", "Rajshahi", "03:30 PM", 45, 1000),# 1000 per seat
        Bus("104", "Khulna", "11:00 PM", 45, 1200), #1200 per seat
    ]

    while True:
        print("\nWelcome to the Bus Ticket Booking System!")
        print("1. View Available Buses")
        print("2. Book a Ticket")
        print("3. View Booking Details")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\nAvailable Buses:")
            for bus in buses:
                bus.display_details()

        elif choice == 2:
            bus_number = input("\nEnter the Bus Number you want to book: ")
            selected_bus = next((bus for bus in buses if bus.bus_number == bus_number), None)

            if selected_bus:
                user_name = input("Enter your name: ")
                try:
                    seats_to_book = int(input("Enter the number of seats to book: "))
                    selected_bus.book_ticket(user_name, seats_to_book)
                except ValueError:
                    print("Invalid input. Seats must be a number.")
            else:
                print("Invalid Bus Number. Please try again.")

        elif choice == 3:
            bus_number = input("\nEnter the Bus Number to view booking details: ")
            selected_bus = next((bus for bus in buses if bus.bus_number == bus_number), None)

            if selected_bus:
                selected_bus.display_bookings()
            else:
                print("Invalid Bus Number. Please try again.")

        elif choice == 4:
            print("Thank you for using the Bus Ticket Booking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
