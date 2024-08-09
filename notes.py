ife=str(input("tienes IFE?\n"))


if ife.lower() == "si":
    edad=int(input("cuantos años tienes?\n"))
    if edad<18:
        print("no puedes entrar")
    else:
        print("entra")
else:
    print("no puedes entrar")