import json

class MovieTicketBooking:
    def __init__(self):
        self.movies = {
            1: {"name": "RRR", "prices": {"Normal": 300, "VIP": 500}},
            2: {"name": "Inception", "prices": {"Normal": 250, "VIP": 450}},
            3: {"name": "Interstellar", "prices": {"Normal": 280, "VIP": 480}},
        }
        self.seats = [[0 for _ in range(5)] for _ in range(5)]  # 5x5 seating grid

    def display_movies(self):
        print("Available Movies:")
        for num, details in self.movies.items():
            print(f"{num}. {details['name']} (Normal: ₹{details['prices']['Normal']}, VIP: ₹{details['prices']['VIP']})")

    def show_seats(self):
        print("\nScreen This Side 🎥")
        for row in range(5):
            print(f"Row {row+1}: ", end="")
            for seat in range(5):
                print("🟩" if self.seats[row][seat] == 0 else "❌", end=" ")
            print()

    def book_seat(self):
        try:
            row = int(input("Enter row number (1-5): ")) - 1
            seat = int(input("Enter seat number (1-5): ")) - 1
            if self.seats[row][seat] == 1:
                print("Seat is already booked!")
                return
            movie_choice = int(input("Enter the number of the movie you want to watch: "))
            if movie_choice not in self.movies:
                print("Invalid movie selection!")
                return
            movie = self.movies[movie_choice]
            seat_type = int(input("Choose Seat Type (1: Normal, 2: VIP): "))
            price = movie['prices']["Normal" if seat_type == 1 else "VIP"]
            confirm = input(f"Confirm booking for ₹{price}? (yes/no): ")
            if confirm.lower() == "yes":
                self.seats[row][seat] = 1
                print("✅ Booking Successful!")
                print("\n🎟 MOVIE TICKET 🎟")
                print("===================")
                print(f"Movie  : {movie['name']}")
                print(f"Seat   : Row {row+1}, Seat {seat+1}")
                print(f"Price  : ₹{price}")
                print("===================\n")
        except (IndexError, ValueError):
            print("Invalid input! Please enter valid numbers.")

    def cancel_booking(self):
        try:
            row = int(input("Enter row number to cancel (1-5): ")) - 1
            seat = int(input("Enter seat number to cancel (1-5): ")) - 1
            if self.seats[row][seat] == 0:
                print("No booking found for this seat.")
                return
            self.seats[row][seat] = 0
            print("✅ Booking Cancelled.")
        except (IndexError, ValueError):
            print("Invalid input! Please enter valid numbers.")

    def run(self):
        while True:
            print("\n1. View Movies\n2. View Seats\n3. Book a Seat\n4. Cancel Booking\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_movies()
            elif choice == "2":
                self.show_seats()
            elif choice == "3":
                self.book_seat()
            elif choice == "4":
                self.cancel_booking()
            elif choice == "5":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    system = MovieTicketBooking()
    system.run()
