skaitli = [4, 7, 2, 9, 7, 1]

try:
    meklejamais = int(input("Ievadi meklējamo skaitli: "))
except ValueError:
    print("Nederīga ievade: jāievada vesels skaitlis.")
else:
    atrastie_indeksi = []

    for indekss in range(len(skaitli)):
        if skaitli[indekss] == meklejamais:
            atrastie_indeksi.append(indekss)

    if len(atrastie_indeksi) == 0:
        print("Nav atrasts")
    else:
        print(f"Pirmais indekss: {atrastie_indeksi[0]}")
        print(f"Visi indeksi: {atrastie_indeksi}")