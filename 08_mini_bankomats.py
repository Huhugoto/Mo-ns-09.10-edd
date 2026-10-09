atlikums = 100

while True:
    print()
    print("1 — apskatīt atlikumu")
    print("2 — iemaksāt naudu")
    print("3 — izņemt naudu")
    print("4 — beigt darbu")

    izvele = input("Izvēlies darbību: ").strip()

    if izvele == "1":
        print(f"Tavs atlikums: {atlikums}")

    elif izvele == "2":
        try:
            summa = float(input("Cik iemaksāt? "))
        except ValueError:
            print("Kļūda: jāievada skaitlis.")
        else:
            if summa <= 0:
                print("Summai jābūt lielākai par 0.")
            else:
                atlikums += summa
                print(f"Iemaksāts: {summa}. Jaunais atlikums: {atlikums}")

    elif izvele == "3":
        try:
            summa = float(input("Cik izņemt? "))
        except ValueError:
            print("Kļūda: jāievada skaitlis.")
        else:
            if summa <= 0:
                print("Summai jābūt lielākai par 0.")
            elif summa > atlikums:
                print("Kontā nepietiek naudas.")
            else:
                atlikums -= summa
                print(f"Izņemts: {summa}. Jaunais atlikums: {atlikums}")

    elif izvele == "4":
        print("Paldies, uz redzēšanos!")
        break

    else:
        print("Nepareiza izvēle. Ievadi 1, 2, 3 vai 4.")