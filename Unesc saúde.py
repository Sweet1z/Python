print("Bem vindo ao UNESC saúde")
name = str (input("Digite seu nome: "))
sexo = str (input("Qual sua sexualidade? M para masculino F para feminino"))
idade = int (input("Digite sua idade: "))
alt_paciente = float (input("Digite sua altura: "))
peso_paciente =  float (input("Digite seu peso: "))

print ("""MENU
       1 - Calcular IMC
       2 - Calcular Taxa metabólica Basal
       3 - Sair """)
opcao = int  (input("Digite a opção desejada: "))

if opcao == 1:
    imc = peso_paciente / (alt_paciente **2)
    print(f"Seu IMC é: {imc:.2f}")
elif opcao == 2:
    if sexo == 'M' or 'm':
        tmb = 66 + (13.7 * peso_paciente) + (5 * alt_paciente) - (6.8 * idade)
        print (f"Sua taxa metabólica basal é {tmb} calorias")
elif sexo == 'F' or 'f':
    tmb = 665 + (9.6 * peso_paciente) + (1.8 * alt_paciente) - (4.7 * idade)
    print (f"Sua taxa metabólica é: {tmb} calorias")
elif opcao == 3:
    print("Obrigado por usar o UNESC saúde!")