# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, train_no, fro, to, fare):
        self.train_no = train_no
        self.fro = fro
        self.to = to
        self.fare = fare
    
    def book_ticket(self):
        print(f"Your ticket is confirmed for {self.fro} to {self.to}.\nThe train number is {self.train_no}")

    def get_status(self):
        print(f"The train {self.train_no} is running on time.")

    def train_fare(self):
        print(f"The ticket fare for the train {self.train_no} form {self.fro} to {self.to} is {self.fare}")


dep_place = ["Kolkata", "Delhi", "Chennai", "Haydrabad"]
arr_place = ["Mumbai", "Bangaluru", "Gujrat", "Punjab"]

obj_1 = Train(randint(33812, 44987), dep_place[randint(0, len(dep_place))-1], arr_place[randint(0, len(arr_place))-1], randint(3000, 7000))
obj_1.book_ticket()
obj_1.get_status()
obj_1.train_fare()