ievade = input("Ievadi veselu skaitli: ").strip()

if not ievade.lstrip("-").isdigit():
    print("Lūdzu, ievadi veselu skaitli.")
else:
    skaitlis = int(ievade)
    for i in range(1, 11):
        print(f"{skaitlis} x {i} = {skaitlis * i}")