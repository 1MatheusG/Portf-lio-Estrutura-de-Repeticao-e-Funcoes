def calcular_media(notas):
    return sum(notas) / len(notas)

def gerenciar_notas_turma():
    media_aprovacao = float(input("Informe a média de aprovação: "))
    
    qtd_alunos = int(input("Informe a quantidade de alunos: "))
    
    alunos = []
    
    for i in range(qtd_alunos):
        print(f"\n--- Aluno {i + 1} ---")
        nome = input("Nome do aluno: ")
        qtd_notas = int(input(f"Quantas notas serão lançadas para {nome}? "))
        notas = []
        
        for j in range(qtd_notas):
            nota = float(input(f"Informe a nota {j + 1}: "))
            notas.append(nota)
        
        media = calcular_media(notas)
        alunos.append({"nome": nome, "notas": notas, "media": media})
    
    print("\n--- Resultados ---")
    aprovados = []
    reprovados = []
    
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        
        if aluno["media"] >= media_aprovacao:
            aprovados.append(aluno["nome"])
        else:
            reprovados.append(aluno["nome"])
    
    print(f"\nTotal de alunos: {qtd_alunos}")
    print(f"Quantidade de aprovados: {len(aprovados)}")
    print("Aprovados:", ", ".join(aprovados))
    print(f"Quantidade de reprovados: {len(reprovados)}")
    print("Reprovados:", ", ".join(reprovados))

gerenciar_notas_turma()
