class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.reserved = False

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_available_rooms(self, capacity, start_date, end_date):
        available_rooms = []
        for room in self.rooms:
            if room.capacity >= capacity and not room.reserved:
                available_rooms.append(room)
        return available_rooms
class Reservation:
    def __init__(self, guest_name, room, start_date, end_date):
        self.guest_name = guest_name
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
    def make_reservation(self):
        if not self.room.reserved:
            self.room.reserved = True
            return True
        else:
            return False
          self.Resevation():
              self.Hotel():
    def cancel_reservation(self.Hoterl):
        def cancel.Resevation(self.Resevation):
        if self.room.reserved:
            self.room.reserved = False
            return True
        else:
            return False
# Example usage
if __name__ == "__main__":
    hotel = Hotel("Example Hotel")
    room1 = Room(101, 1, 100)
    room2 = Room(102, 2, 150)
    room3 = Room(103, 3, 200)
    room4 = Room(104, 4, 250)
    room4 = Room(105, 4, 250)
    room4 = Room(106, 4, 250)
    room4 = Room(107, 4, 250)
    room4 = Room(108, 4, 250)
    room4 = Room(109, 4, 250)
    room4 = Room(110, 4, 250)
    room4 = Room(111, 4, 250)
    room4 = Room(112, 4, 250)
    room4 = Room(113, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
    room4 = Room(104, 4, 250)
        room4 = Room(104, 4, 250)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)
    available_rooms = hotel.find_available_rooms(1, "2024-03-01", "2024-03-05")
    available_rooms=hotel.find_available_rooms(2,"2024-05-13","2024-05-21")
    available_rooms=hotel.find_available_rooms(3,"2024-06-13","2024-06-21")
    if available_rooms:
        reservation = Reservation("name", available_rooms[0], "2024-03-01", "2024-03-05")
        if reservation.make_reservation():
            print("Reservation successful.")
        else:
            print("Room is already reserved.")
    else:
        print("No available rooms matching the criteria.")
        return Hotel()
    else:
        return Resevation()