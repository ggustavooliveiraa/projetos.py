def Listador_3000_strings (lista, quantidade):
    for i in range (quantidade):
        lista.append(input("Nome do exercício: "))
    return lista

def Meta_semanal(caloria_queimada, Queima_desejada):
    if caloria_queimada >= Queima_desejada:
        fogo_de_artificio = """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡆⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀
⠀⠀  ⠀⠠⢤⣦⠤⠀⠀⠉⢏⠀⠠⣤⣦⠄⠀⡸⠁⠀⠀⠀⣠⠹⠛⠏⠀⠀⠀⠀
    ⠀⣠⠀⠀⠉⠈⠐⢄⠀⠀⠈⢆⠀⠉⡏⠀⠰⠁⠀⠀⠠⠊⠀⠀⠠⢤⣦⡤⠀⠀
    ⠘⠛⠋⠒⠂⠤⢀⠀⠁⠀⣀⠀⠀⠀⠣⢤⣦⡤⠀⠁⠀⡀⠤⠒⠉⠈⠈⠁⠀⠀
⠀⠀  ⢠⣶⡄⠀⣀⣀⠀⠙⠛⢋⡀⠀⠀⡸⠉⠁⠀⠀⣁⡀⠠⠤⠄⠾⠷⠂⠀⠀
    ⣀⣤⣀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠈⠀⠐⠀⠀⠀⠁⢤⣶⡄⠀⠀⣀⣀⡀⣀⣠⣀
    ⠘⠉⠁⠀⠀⠀⢀⡠⠄⠂⠀⡠⠀⠀⠀⠐⢄⠀⠀⠂⠠⠄⣀⠀⠀⠀⠀⠘⠛⠃
⠀⠀⠀ ⣶⣶⠉⠁⠀⢀⣄⠞⠀⠀⠀⡄⠀⠀⠑⠄⡀⠀⠀⠀⠉⢳⣾⡖⠀⠀⠀
⠀⠀⠀⠀    ⠀⠀⠀⠀⠙⠛⠃⠀⠠⣴⣦⠄⠀⠈⠝⠛⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
        print(fogo_de_artificio, "\n BOA CAMPEÃ(O)")

        return f"~~~ META ATINGIDA, ÔNUS DE: {caloria_queimada - Queima_desejada} cal ~~~ \n ~~~~ VITÓRIA, O BEM VENCEU ᕦ( ᐛ )ᕤ ~~~ "
    elif Queima_desejada > caloria_queimada:
        return f"~~~ Quase lá, não foi dessa vez. A linha de chagada está logo ali. Faltam: {Queima_desejada - caloria_queimada} cal ~~~ ( ◡̀_◡́)ᕤ"
   


def relatorio_diario():
    quantidade_exercicios = int(input("Quantidade de série(s) realizada(s): "))
    
    print("Digite o nome dos exercícios:")
    exercicios_realizados = Listador_3000_strings([], quantidade_exercicios)
    
    tempo_da_sessao = int(input("Quanto tempo durou a sessão de hoje (min): "))
    calorias_queimadas = float(input("Calorias queimadas: "))
    media_calorica_por_exercicio = calorias_queimadas/quantidade_exercicios
    
    # lista: [lista_de_exercicios, tempo, calorias, media de queima/exercicio]
    resumo = [exercicios_realizados, tempo_da_sessao, calorias_queimadas, media_calorica_por_exercicio]
    
    print("\n~~~ Resumo do dia ᕙ(⇀‸↼‵‵)ᕗ ~~~")
    print("Exercícios realizados:", ", ".join(exercicios_realizados))
    print("Tempo total:", tempo_da_sessao, "min")
    print("Calorias queimadas:", calorias_queimadas, "kcal")
    print("Média de calorias queimadas por exercício: ",media_calorica_por_exercicio)
    
    return resumo

def registrador():
    historico = []
    continuar = "s"

    while continuar.lower() == "s":
        dia = relatorio_diario()
        historico.append(dia)
        continuar = input("Deseja registrar outro dia? (s/n): ")

    # Soma de calorias
    total_calorias = sum(dia[2] for dia in historico)  # Índice 2 = calorias
    soma_medias = sum(dia[3] for dia in historico) # Índice 3 = media de calorias por exercicio
    media_geral = soma_medias/ len(historico)
    
    print("\nResumo geral:")
    print(f"Total de dias registrados: {len(historico)}")
    print(f"Total de calorias queimadas: {total_calorias:.2f} cal")
    print(f"Média de calorias queimadas por exercício ao longo da semana: {media_geral:.2f} cal")

    return total_calorias 


def IMC(peso, altura):
    IMC = peso/(altura**2)
    
    if IMC < 18.5:
        return f"Seu IMC é de {IMC}, consideramos esse resultado como Baixo Peso. \n É aconselhado a procura de um médico e nutricionista"
    elif IMC > 18.5 and IMC < 25:
        return f"Seu IMC é de {IMC}, consideramos esse resultado como Adequado. \n ~~~ BOA, VAMOS CONTINUAR ASSIM ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ ~~~ "
    elif IMC >= 25 and IMC <= 29.9:
        return f"Seu IMC é de {IMC}, consideramos esse resultado como Sobrepreso. \n ~~~ (૭ ｡•̀ ᵕ •́｡ )૭ UFF, NA TRAVE. ESTAMOS QUASE LÁ ~~~"
    elif IMC >= 30:
        return f" Seu IMC é de {IMC}, consideramos esse resultado como Obesidade. \n ~~~ SEM PROBLEMAS, COM DETERMINAÇÃO E DILIGÊNCIA A GENTE SUPERA QUALQUER DOENÇA ~~~"
    




print(r"""
        (•̀ᴗ•́ )
　　＿ノ ヽ ノ＼ __
　 /　`/ ⌒Ｙ⌒ \ ` \
　|　ﾉ⌒＼ ￣￣ヽ　 ノ
　ヽ＿＿＿＞､＿＿_／
　　　 ｜( 王 ﾉ〈
　　　 /ﾐ`ー―彡\
""")
print ("~~~ E AÍ CAMPEÃO, VAMO FICA GRANDÃO? ~~~")
Queima_desejada = float(input("~~~ QUAL A MISSÃO DA SEMANA, CAPITÃO? QUANTAS cal QUER QUEIMAR?: "))
Dias = int(input("~~~ COMO VAMOS FAZER ISSO, CHEFE?, QUAL A SUA DISPOSIÇÃO SEMANAL(quantos dias)?: "))
print(f"~~~~ Missão registrada: {Queima_desejada} cal em {Dias} dias, VAMO QUE VAMO! ~~~ ᕙ(  •̀ ᗜ •́  )ᕗ")

print("Antes de prosseguirmos, vamos registrar uns dados para comparar o antes com o depois")
IMC_inicial = IMC(int(input("Qual o teu peso?: ")), float(input("Qual a tua altura?: ")))
print(IMC_inicial)

print("~~~FIM DO DIA CHEFE, VAMOS VER COMO NOS SAÍMOS ~~~")
#relatorio diario
total_calorias_queimadas = registrador()
resultado_meta = Meta_semanal(total_calorias_queimadas, Queima_desejada)
print(resultado_meta)

querer =  input("Gostaria de comparar o teu IMC do início com o de agora? (s/n): ")
if querer.lower() == "s":
    IMC_final = IMC(int(input("Qual o teu peso?: ")), float(input("Qual a tua altura?: "))) #provavel ordem = dps do relatorio semanal -> sexta
    print(IMC_final)
elif querer.lower() == "n":
    print("OK. Sem problemas.")

print("Por aqui encerramos, muito obrigado por comparecer as sessões. Esperamos você aqui na semana que vem, até logo.")