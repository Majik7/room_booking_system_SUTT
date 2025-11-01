import csv
from roomManager import roomManager

print("Welcome to the Room Booking System")

manager = roomManager()

try:
    manager.csvLoad()

except(FileNotFoundError):
    with open("bookings_final_state.csv", 'w', newline='') as f:
        wrt = csv.writer(f)
        wrt.writerow(["room_no", "building", "capacity", "booked_hours"])    
        
ans = 'y'
while ans in "yY":
    opt = int(input("What would you like to do \n 1. Display room details \n 2. Create a new room " \
    "\n 3. Book a room \n 4. Filter and find rooms \n 5. Exit \n - "))

    if opt == 1:
        rno = input("Enter room number to search for - ")

        try:
            manager.printRoomData(rno)
        except Exception as e:
            print(e)

    elif opt == 2:
        rno = input("Enter room number to add - ")
        building = input("Enter building the room is in - ")
        capacity = int(input("Enter room capacity - "))

        try:
            manager.addroom(rno, building, capacity)
        except Exception as e:
            print(e)

    elif opt == 3:
        rno = input("Enter room number to book - ")
        hour = int(input("Enter an hour from 0-23 to book the room for 1 hour - "))

        if hour < 0 or hour > 23:
            print("Invalid hour entered")
            continue

        try:
            manager.bookRoom(rno, hour)
        except Exception as e:
            print(e)

    elif opt == 4:
        building = input("Enter building (enter if not filtering building) - ")
        capacity = input("Enter capacity of room (enter if not filtering capacity) - ")
        free_hour = input("Enter an hour to check (enter if not filtering free hours) - ")

        building = building if building else None
        capacity = int(capacity) if capacity else None
        free_hour = int(free_hour) if free_hour else None

        try:
            manager.filterAndFind(building, capacity, free_hour)
        except Exception as e:
            print(e)

    elif opt == 5:
        ans = 'n'

    else:
        print("Invalid option!")

manager.csvDump()