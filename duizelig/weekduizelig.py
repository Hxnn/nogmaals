while True:
    day = input('Kies een dag van de week, ma, di, wo, do, vr, za, zo. ')

    if day == "ma":
        print('ma')
    elif day == "di":
        print("ma, di")
    elif day == "wo":
        print("ma, di, wo")
    elif day == "do":
        print("ma, di, wo, do")
    elif day == "vr":
        print("ma, di, wo, do, vr")
    elif day == "za":
        print("ma, di, wo, do, vr, za")
    elif day == "zo":
        print("ma, di, wo, do, vr, za, zo")
    else:
        print("Dit was geen optie!")
    break
