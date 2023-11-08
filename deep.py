a = input("Qual a respota para as grandes perguntas da vida e do universo e de tudo mais?")

b = a.lower().replace("-","").replace(" ","")

if b == "fortytwo" or b == "42":
        print("Yes")
else:
        print("No")