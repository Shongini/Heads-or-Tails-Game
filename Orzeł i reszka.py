import random
import time

# poczatkowy wynik gracza i komputera
gracz = 0
komputer = 0

print("Orzeł czy Reszka?")
print("Jeśli chcesz zamknąc grę, kliknij 'Z'.")

while True:
    #wybór gracza
    x = input()
    if x == 'Z' :
        break
    elif x == 'o' :
        x = "orzeł"
    elif x == 'r' :
        x = "reszka"
    else:
        print("Dokonaj wyboru: ")
        print("o - Orzeł")
        print("r - Reszka")
        print("Z - Zamknij grę")
    #w sytuacji innego wyboru, powrót do początku
    continue
    #rzut moneta
    y = random.choice(["orzeł", "reszka"])

    #odliczanie 3 sekund
    for i in range (0,3):
        print(3-i)
        time.sleep(1)

    print("Wynik rzutu: ", y)

    #kto wygrał
    if x == y:
        gracz+=1
    else:
        komputer+=1

    #statystyka końcowa
    print("Wynik rozgrywki: ")
    print("Gracz: ", gracz)
    print("Komputer: ", komputer)