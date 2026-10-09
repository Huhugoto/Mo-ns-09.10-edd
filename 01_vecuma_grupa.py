BERNS_LIDZ = 12       
PUSAUDZIS_LIDZ = 17  
PIEAUGUSAIS_LIDZ = 64  
ievade = input("Ievadi savu vecumu: ").strip()

if ievade == "":
    print("Nekas netika ievadīts.")
else:
    try:
        vecums = int(ievade)
    except ValueError:
        print("Lūdzu, ievadi veselu skaitli.")
    else:
        if vecums < 0:
            print("Vecums nevar būt negatīvs.")
        elif vecums <= BERNS_LIDZ:
            print("bērns")
        elif vecums <= PUSAUDZIS_LIDZ:
            print("pusaudzis")
        elif vecums <= PIEAUGUSAIS_LIDZ:
            print("pieaugušais")
        else:
            print("seniors")