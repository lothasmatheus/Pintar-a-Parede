r = "S"
while r == "S":
    largura = float(input("Largura da parede: "))
    altura = float(input("Altura da parede: "))
    area = largura * altura
    print("Sua parede tem dimenssão de {:2}x{:2} e sua área é de {}m².".format(largura,altura,area))
    tinta = area / 2 
    print("Para pintar sua parede, é necessário {}L de tinta.".format(tinta))
    r = str(input("Deseja fazer novamente? [S/N] \n\n")).upper()
