def badge_maker(name):
    return (f"Hello. My name is {name}")

def batch_badge_creator(names):
    name_messages = []
    for name in names:
        name_messages.append(f'Hello, my name is {name}')
    return name_messages

def assign_rooms(names):
    rooms_list=[f"Hello {name}! You'll be assigned to room 1" for name in names]
    return rooms_list
   
def printer(names):
    badge_messages = batch_badge_creator(names)
    for message in badge_messages:
        print(message)

    rooms_placed = assign_rooms(names)
    for room in rooms_placed:
        print (room)
