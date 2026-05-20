print("=== Calculator ===")

while True:
    print("\n transactions:")
    print("1 -> Addition")
    print("2 -> Substraction")
    print("3 -> Multiplation")
    print("4 -> Division")
    print("5 -> Taking Base")
    print("6 -> Exit")

    secim = input("Select a process: ")

    if secim == "6":
        print(".")
        break

    if secim not in ["1", "2", "3", "4", "5"]:
        print("You made an invalid choice. ")
        continue

    sayi1 = float(input("Enter the first number: "))
    sayi2 = float(input("Enter the second number: "))

    if secim == "1":
        sonuc = sayi1 + sayi2
        print("result:", sonuc)

    elif secim == "2":
        sonuc = sayi1 - sayi2
        print("result:", sonuc)

    elif secim == "3":
        sonuc = sayi1 * sayi2
        print("result:", sonuc)

    elif secim == "4":
        if sayi2 == 0:
            print("can't divide 0")
        else:
            sonuc = sayi1 / sayi2
            print("result:", sonuc)

    elif secim == "5":
        sonuc = sayi1 ** sayi2
        print("result:", sonuc)