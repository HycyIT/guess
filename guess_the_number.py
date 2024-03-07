import random
random_number = random.randint(1, 100)


def guessNumbers():
    while True:
        try:
            num = int(input("Podaj liczbę : "))
            if (num > random_number):
                print(f"Liczba {num} jest za duża podaj mniejszą")
            elif (num < random_number):
                print(f"Liczba {num} jest za mała, podaj większą")
            else:
                print(f"Brawo chodziło mi o liczbę {num}")
                break
        except ValueError:
            print("Miałeś podać liczbę")


guessNumbers()
