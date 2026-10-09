try:
    daudzums = int(input("Cik skaitļus ievadīsi? "))
except ValueError:
    print("Kļūda: jāievada vesels skaitlis.")
else:
    if daudzums <= 0:
        print("Skaitļu skaitam jābūt lielākam par 0.")
    else:
        summa = 0
        pozitivi = 0
        negativi = 0
        nulles = 0
        pari = 0
        nepari = 0

        for i in range(1, daudzums + 1):
            while True:
                try:
                    skaitlis = int(input(f"Ievadi {i}. skaitli: "))
                    break
                except ValueError:
                    print("Lūdzu, ievadi veselu skaitli.")

            summa += skaitlis

            if skaitlis > 0:
                pozitivi += 1
            elif skaitlis < 0:
                negativi += 1
            else:
                nulles += 1

            if skaitlis % 2 == 0:
                pari += 1
            else:
                nepari += 1

        videjais = summa / daudzums

        print(f"Summa: {summa}")
        print(f"Pozitīvi: {pozitivi}, negatīvi: {negativi}, nulles: {nulles}")
        print(f"Pāra: {pari}, nepāra: {nepari}")
        print(f"Vidējais aritmētiskais: {videjais}")