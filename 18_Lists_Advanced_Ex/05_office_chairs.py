number_of_rooms = int(input())
room_number = 0
game_on = True
total_free_chairs = 0

for room in range(number_of_rooms):
    chairs, visitors = input().split()
    room_number += 1
    if len(chairs) < int(visitors):
        print(f"{int(visitors) - len(chairs)} more chairs needed in room {room_number}")
        game_on = False
    total_free_chairs += len(chairs) - int(visitors)

if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")
