PAREIZA_PAROLE = "46"
MAKS_MEGINAJUMI = 3

meginajumi = 0

while meginajumi < MAKS_MEGINAJUMI:
    parole = input("Ievadi paroli: ")
    meginajumi += 1

    if parole == PAREIZA_PAROLE:
        print("Piekļuve atļauta")
        break

    atlicis = MAKS_MEGINAJUMI - meginajumi
    if atlicis > 0:
        print(f"Nepareiza parole. Atlikušie mēģinājumi: {atlicis}")
else:
    print("Piekļuve bloķēta")