import math


def sup1(a, b, c, delta):
    x1 = (-b -math.sqrt(delta)) / (2 * a)
    x2 = (-b +math.sqrt(delta)) / (2 * a)
    print(f"Le resultat de x1 est {x1}.")
    print(f"Le resultat de x2 est {x2}.")
    main()

def equal1(a, b, c):
    x = -b / (2 * a)
    print(f"Le résultat de l'équation avec les valeurs {a, b, c} est {x}")
    main()

def main():
    print("----------\nRésolveur d'équation du second degrès")
    a = int(input("Valeur de a: "))
    b = int(input("Valeur de b: "))
    c = int(input("Valeur de c: "))
    print(f"Voici les valeurs que vous avez entrés a={a} b={b} c={c}")
    # Formule pour calculer Delta
    delta = (b*b) - 4 * a * c
    print("Δ est égal à:", delta)
    if delta == 0:
        equal1(a, b, c)
    if delta < 0:
        print("Il n'y a pas de solution réelle pour cette équation.")
        main()
    if delta > 0:
        sup1(a, b, c, delta)

    


main()