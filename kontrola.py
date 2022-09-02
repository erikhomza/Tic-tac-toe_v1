def kontrola1():
    global hra
    global jkl
    global hrac_1_vytazstva
    global hrac_2_vytazstva
    if jkl[0] == "x" and jkl[1] == "x" and jkl[2] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "x" and jkl[4] == "x" and jkl[5] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[6] == "x" and jkl[7] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "x" and jkl[3] == "x" and jkl[6] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1] == "x" and jkl[4] == "x" and jkl[7] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "x" and jkl[5] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "x" and jkl[4] == "x" and jkl[8] == "x":
        print("Hráč 1 vyhral.")
        hrac_1_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "x" and jkl[4] == "x" and jkl[6] == "x":
        print("Hráč 1 vyhral.")
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
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "O" and jkl[4] == "O" and jkl[5] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[6] == "O" and jkl[7] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "O" and jkl[3] == "O" and jkl[6] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[1] == "O" and jkl[4] == "O" and jkl[7] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[3] == "O" and jkl[5] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[0] == "O" and jkl[4] == "O" and jkl[8] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    elif jkl[2] == "O" and jkl[4] == "O" and jkl[6] == "O":
        print("Hráč 2 vyhral.")
        hrac_2_vytazstva += 1
        print(f"Hráč 1 vyhral {hrac_1_vytazstva} hier a hráč 2 vyhral {hrac_2_vytazstva} hier.")
        hra = False
        nova_hra()
    else:
        pass