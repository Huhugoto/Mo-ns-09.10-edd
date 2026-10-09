try:
    daudzums = int(input("Cik skaitļus ievadīsi? "))
except ValueError:
    print("Kļūda: jāievada vesels skaitlis.")
else:
    if daudzums <= 0:
        print("Skaitļu skaitam jābūt lielākam par 0.")
    else:
        mazakais = None
        lielakais = None

        for i in range(1, daudzums + 1):
            while True:
                try:
                    skaitlis = int(input(f"Ievadi {i}. skaitli: "))
                    break
                except ValueError:
                    print("Lūdzu, ievadi veselu skaitli.")

            if mazakais is None:
                mazakais = skaitlis
                lielakais = skaitlis
            else:
                if skaitlis < mazakais:
                    mazakais = skaitlis
                if skaitlis > lielakais:
                    lielakais = skaitlis

        print(f"Mazākais: {mazakais}")
        print(f"Lielākais: {lielakais}")