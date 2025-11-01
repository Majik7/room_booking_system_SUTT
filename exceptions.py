class RoomNotFoundError(Exception):
    def __str__(self):
        print()
        return "The room requested does not exist"
    
class TimeslotAlreadyBookedError(Exception):
    def __str__(self):
        print()
        return "The requested time slot is already booked"
    
class RoomAlreadyExistsError(Exception):
    def __str__(self):
        print()
        return "The room number already exists"