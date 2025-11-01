from exceptions import *
from room import *
import csv

class roomManager:
    def __init__(self):
        self.roomdict = {}

    def addroom(self, room_no, building, capacity):
        newroom = Room(room_no, building, capacity, None)

        if room_no in self.roomdict:
            raise RoomAlreadyExistsError()
        else:
            self.roomdict[room_no] = newroom
            print(f"Room number {room_no} created succesfully")

    def printRoomData(self, room_no):
        if room_no in self.roomdict:
            room = self.roomdict[room_no]
            print(f"Room no - {room_no}")
            print(f"Building - {room.building}")
            print(f"Capacity - {room.capacity}")
            print(f"Booked hours - {room.booked_hours.replace(';', ',')}")

        else:
            raise RoomNotFoundError()
        
    def bookRoom(self, room_no, hour):
        if room_no in self.roomdict:
            room = self.roomdict[room_no]
            room.booked_hours = "" if room.booked_hours is None else room.booked_hours
            bookedlist = room.booked_hours.split(";")
            
            if str(hour) not in bookedlist:
                if len(room.booked_hours) == 0:
                    room.booked_hours = str(hour)
                
                else:
                    room.booked_hours += f";{hour}"

                print()
                print(f"Room {room_no} succesfully booked at hour {hour}")
                print()

            else:
                raise TimeslotAlreadyBookedError()

        else:
            raise RoomNotFoundError()
        
    def filterAndFind(self, building: str | None = None, capacity: int | None = None, free_hours: int | None = None):
        if (building is None and capacity is None and free_hours is None):
            print()
            print("Please enter filter conditions")
            print()

            return
        
        filteredlist = []

        for i in self.roomdict:
            room = self.roomdict[i]
            if ((room.building == building or building is None) and (room.capacity == capacity or capacity is None) and (str(free_hours) not in room.booked_hours.split(';') or free_hours is None)):
                filteredlist += [i]
        
        else:
            if len(filteredlist):
                print()
                print("The following rooms satisfy the given conditions")
                for i in filteredlist:
                    print(f"Room {i}")
            
            else:
                print("No such rooms were found")

        print()

    def csvDump(self):
        with open("bookings_final_state.csv", "w", newline='') as f:
            wrt = csv.writer(f)
            wrt.writerow(["room_no", "building", "capacity", "booked_hours"])

            for i in self.roomdict:
                room = self.roomdict[i]
                wrt.writerow([i, room.building, room.capacity, room.booked_hours])

            else:
                print()
                print("data dumped into csv successfully")
                print()

    def csvLoad(self):
        with open("bookings_final_state.csv", "r", newline='') as f:
            rdr = csv.reader(f)
            next(rdr)

            for i in rdr:
                self.roomdict[i[0]] = Room(i[0], i[1], int(i[2]), i[3]) # room no, building, cap, booking

            else:
                print()
                print("data loaded successfully from csv")
                print()