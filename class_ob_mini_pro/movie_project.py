
class movie:
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int,booked_seats:int):
        self.movie_name=input("Enter the movie name: ")
        self.total_seats=int(input("Enter the total seats: "))
        self.ticket_price=int(input("Enter the ticket price: "))
        self.booked_seats=int(input("Enter the booked seats: "))

    def book_ticket(self,number_of_ticket:int)->None:
        if self.booked_seats+number_of_ticket>self.total_seats:
            print("Sorry, not enough seats available.")
        else:
            self.booked_seats+=number_of_ticket
            print(f"{number_of_ticket} tickets booked successfully for {self.movie_name}.")
            print(f"Total booked seats: {self.booked_seats}")


    def show_status(self)->None:
                print(f"Movie Name: {self.movie_name}")
                print(f"Total Seats: {self.total_seats}")
                print(f"Booked Seats: {self.booked_seats}")
                print(f"Available Seats: {self.total_seats - self.booked_seats}")
                print(f"Ticket Price: {self.ticket_price}")
    

movie1=movie("Inception",100,10,20)
movie1.book_ticket(30)
movie1.show_status()