nota1 = float(input("\nDigite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

md = (nota1 + nota2 + nota3 + nota4) /4
print(f"\nSua media foi de {md:.2f}")
print("\n")

if md >= 7:
    print("você foi aprovado!\n")

if md < 3:
    print("Você esta reprovado :()\n")

if md <7 and md >= 3:
    print("Você precisa fazer a recuperação!\n")
    avs = float(input("Qual foi a nota da sua recuperação?: "))

    if avs >= 7:
        print("\nVocê esta aprovado!\n")
    else:
        print("\nVocê esta reprovado :(\n")    
