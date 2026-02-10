placa = input("Placa do veículo: ")
nome = input("Nome do motorista: ")
velocidade_registrada = float(input("Digite a velocidade registrada: "))
velocidade_permitida = float(input("Digite a velocidade permitida: "))
reincidencia = input("O motorista já foi multado antes? (sim/não): ").lower()

multa = 0.0
infracao = False
pontos = 0

if velocidade_registrada <= velocidade_permitida:
    print("Nenhuma infração registrada.")

elif velocidade_registrada <= velocidade_permitida * 1.2:
    infracao = True
    multa = 130.16
    pontos = 0
    print("Infração leve")
    print("Multa: R$ 130,16 | Pontos: 0")

elif velocidade_registrada <= velocidade_permitida * 1.5:
    infracao = True
    multa = 195.23
    pontos = 5
    print("Infração grave")
    print("Multa: R$ 195,23 | Pontos: 5")

else:
    infracao = True
    multa = 880.41
    pontos = 7
    print("Infração gravíssima")
    print("Multa: R$ 880,41 | Pontos: 7")
    print("CNH suspensa!")
    print("Compareça ao Detran e faça o curso de reciclagem.")

if infracao:
    if reincidencia == "sim":
        multa *= 2
        print("Atenção: multa dobrada por reincidência.")

    pagamento = input("Deseja pagar a multa agora? (sim/não): ").lower()

    if pagamento == "sim":
        valor_final = multa * 0.8
        print(f"Pagamento realizado com 20% de desconto.")
        print(f"Valor final: R$ {valor_final:.2f}")
    else:
        print(f"Valor da multa: R$ {multa:.2f}")
