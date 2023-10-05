print("Bem vindo ao quiz do Nóbrega :) \n")
answer_user = input("Quer começar o quiz? (S/N)")

if answer_user != "S":
    quit()

score = 0    

print("Começando...")
print("Pergunta 1: O que eu mais gosto de comer? \n (a) Hamburguer \n (b) Pizza \n (c) Sushi \n (d) Batata Frita \n")
answer_1 = input("Resposta: ")

if answer_1 == "b":
    print("Respota Correta! \n")
    score = score + 1
else:
    print("Resposta Errada :( \n")

    print("Pergunta 2: Quantas tatuagens eu tenho? \n (a) 2 \n (b) 4 \n (c) 3 \n (d) 5 \n")
answer_1 = input("Resposta: ")

if answer_1 == "d":
    print("Respota Correta! \n")
    score = score + 1
else:
    print("Resposta Errada :( \n")

    print("Pergunta 3: Qual País que eu tenho mais vontade de conhecer? \n (a) Alemanha \n (b) Argentina \n (c) Jamaica \n (d) Suiça ")
answer_1 = input("Resposta: ")

if answer_1 == "d":
    print("Resposta Correta! \n")
    score = score + 1
else: 
    print("Resposta Errada :( \n")

    print("Pergunta 4: Qual animal eu tenho em casa? \n (a) Hamster \n (b) Gato \n (c) Jabuti \n (d) Cachorro ")
answer_1 = input("Resposta: ")

if answer_1 == "b":
    print("Resposta Correta! \n")
    score = score + 1
else: 
    print("Resposta Errada :( \n")

    print("Pergunta 5: Qual moto vou comprar em dezembro/2023 ? \n (a) BAJAR DOMINAR 160 \n (b) FZ15 2023 \n (c) CB TWISTER 300F \n (d) CG TITAN 160 ")
answer_1 = input("Resposta: ")

if answer_1 == "a":
    print("Resposta Correta! \n")
    score = score + 1
else: 
    print("Resposta Errada :( ")

print(f"Fim de jogo... \nSua pontuação foi: {score}/5")



