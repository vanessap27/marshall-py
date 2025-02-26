dusa = int(input("how big is dusa? "))

while True:
    yobi = int(input("how big is this yobi? "))
    if dusa > yobi:
        dusa = dusa + yobi
        print(f"Dusa ate yobi! He is size {dusa} and will keep eating ")
    elif dusa < yobi or dusa == yobi:
        print("dusa ran away! ")
        break 