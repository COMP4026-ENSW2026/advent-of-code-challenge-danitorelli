with open(
    "advent-of-code-challenge-danitorelli/01-advent-of-code-challenge/04/sample.in", "r"
) as f:
    linhas = f.readlines()
    pares_atribuidos = [entrada.strip() for entrada in linhas]


pares = 0
for entrada in pares_atribuidos:
    par1, par2 = entrada.split(",")
    par1 = [int(i) for i in par1.split("-")]
    par2 = [int(i) for i in par2.split("-")]

    if par1[0] <= par2[0] and par1[1] >= par2[1]:
        pares += 1
    elif par2[0] <= par1[0] and par2[1] >= par1[1]:
        pares += 1

print(pares)

