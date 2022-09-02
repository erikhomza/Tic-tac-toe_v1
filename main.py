jkl = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
hrac_1_vytazstva = 0
hrac_2_vytazstva = 0
hra = True



def nova_hra():
    global jkl
    global hra
    print("Keď chceš hrať znova napíš 1 inak napíš 0.")
    restart = input()
    if restart == "1":
        jkl = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        hra = True
        piskorky()
    elif restart == "0":
        quit()
    else:
        nova_hra()


def kontrola1():
    global hra
    global jkl
    global hrac_1_vytazstva
    global hrac_2_vytazstva
    if jkl[0] == "x" and jkl[1] == "x" and jkl[2] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "x" and jkl[4] == "x" and jkl[5] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[6] == "x" and jkl[7] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "x" and jkl[3] == "x" and jkl[6] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1] == "x" and jkl[4] == "x" and jkl[7] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "x" and jkl[5] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "x" and jkl[4] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "x" and jkl[4] == "x" and jkl[6] == "x":
        print("Hráč 1 vyhral.")
        hracia_plocha(jkl)
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    else:
        pass


def kontrola2():
    global jkl
    global hra
    global hrac_1_vytazstva
    global hrac_2_vytazstva
    if jkl[0] == "O" and jkl[1] == "O" and jkl[2] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "O" and jkl[4] == "O" and jkl[5] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[6] == "O" and jkl[7] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "O" and jkl[3] == "O" and jkl[6] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1] == "O" and jkl[4] == "O" and jkl[7] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "O" and jkl[5] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "O" and jkl[4] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "O" and jkl[4] == "O" and jkl[6] == "O":
        print("Hráč 2 vyhral.")
        hracia_plocha(jkl)
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    else:
        pass

def hracia_plocha(jkl):
    print(" ", "1", "2", "3")
    print("A", jkl[0], jkl[1], jkl[2])
    print("B", jkl[3], jkl[4], jkl[5])
    print("C", jkl[6], jkl[7], jkl[8])

def hrac1():
    print("Na rade je hráč 1.")
    print("Napíš číslo od 0 po 8.")
    tah = input()
    if tah == "0" or tah == "1" or tah == "2" or tah == "3" or tah == "4" or tah == "5" or tah == "6" or tah == "7" or tah == "8":
        if jkl[int(tah)] == "-":
            jkl[int(tah)] = "x"
        else:
            print("Chybný ťah.")
            hrac1()
    else:
        print("Chybný ťah.")
        hrac1()

def hrac2():
    print("Na rade je hráč 2.")
    print("Napíš číslo od 0 po 8.")
    tah = input()
    if tah == "0" or tah == "1" or tah == "2" or tah == "3" or tah == "4" or tah == "5" or tah == "6" or tah == "7" or tah == "8":
        if jkl[int(tah)] == "-":
            jkl[int(tah)] = "O"
        else:
            print("Chybný ťah.")
            hrac2()
    else:
        print("Chybný ťah.")
        hrac2()

def piskorky():
    global hra
    global jkl
    hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        hrac2()
        kontrola2()
        hracia_plocha(jkl)
    if hra:
        hrac1()
        kontrola1()
        hracia_plocha(jkl)
    if hra:
        print("Remíza.")
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        nova_hra()
piskorky()