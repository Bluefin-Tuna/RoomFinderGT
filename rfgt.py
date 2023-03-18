import requests
from collections import defaultdict

j = requests.get("https://housing.gatech.edu/available-rooms-dir/FreeRooms.json")
j = j.json()
print(j[0]["LastUpdated"])

valid_rooms = defaultdict(set)
num_person = 8
all_open = True
num_roommates = 4

for i in range(len(j) - num_person - 1):
    e = j[i]
    if e['Gender'] not in ["Male", "Dynamic"] or e["Capacity"] != f"{num_person} person":
        continue
    room = e["RoomNumber"][0:-1]
    c = 0
    for r in j[i: i + num_person]:
        if room == r["RoomNumber"][0:-1]: c += 1 
    if c >= num_person and all_open == True:
        valid_rooms[e["BuildingName"]].add(room)
    elif c >= num_roommates and all_open == False:
        valid_rooms[e["BuildingName"]].add(room)
    else:
        continue

for vr in valid_rooms.keys():
    print(vr)
    print(valid_rooms[vr])
    print("\n")