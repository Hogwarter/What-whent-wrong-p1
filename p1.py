print("Henkilö 1:")
nimi1 = input("Nimi:")
ika1 = int(input("Ikä:"))
print("Henkilö 2:")
nimi2 = input("Nimi:")
ika2 = int(input("Ikä:"))
if ika1 == ika2:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")
elif ika1 > ika2:
    print(f"Vanhempi on {nimi1}")
else ika1 < ika2:
    print(f"Vanhempi on {nimi2}")