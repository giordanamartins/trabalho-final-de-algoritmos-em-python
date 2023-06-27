# variáveis globais (matrizes)
alunos = []
treinos = []

# classe aluno
class Aluno:
  nome = None
  cpf = None
  peso = 0
  altura = 0
  status = None

# classe exercícios
class Exercicio:
  nome_exercicio = None
  num_repeticoes = 0
  peso_exercicio = 0

# função de validação de cpf
def validar_cpf(cpf):
    # remover pontos e traços do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    # confere se tem 11 dígitos e se são apenas números
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    else:
        return cpf

# função de cadastro de aluno
def cadastrar_aluno():
    novo_aluno = Aluno()

    novo_aluno.nome = input("Nome: ")
    novo_aluno.cpf = input("CPF: ")
    teste = validar_cpf(novo_aluno.cpf)
    while not teste:
        print("CPF inválido. Tente novamente.")
        novo_aluno.cpf = input("CPF: ")
        teste = validar_cpf(novo_aluno.cpf)
    novo_aluno.cpf = teste
    novo_aluno.peso = float(input("Peso: "))
    novo_aluno.altura = float(input("Altura: "))
    novo_aluno.status = False

    alunos.append(novo_aluno)
    # adicionar novo treino vazio
    treino_vazio = []
    treinos.append(treino_vazio)

    print("Novo aluno cadastrado com sucesso!")

# funções de gerenciamento de treinos
# função do menu de gerenciamento de treino
def gerenciar_treino():
    nome_aluno = input("Digite o nome do aluno: ")
    indice_aluno = buscar_aluno(nome_aluno)

    if indice_aluno == -1:
        print("Aluno não encontrado.")
        return

    aluno = alunos[indice_aluno]
    treino = treinos[indice_aluno]

    print("Menu de Gerenciamento de Treino:")
    print("1 - Incluir novo exercício")
    print("2 - Alterar exercício existente")
    print("3 - Excluir exercício")
    print("4 - Excluir todos os exercícios")
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        incluir_exercicio(indice_aluno)
    elif opcao == 2:
        alterar_exercicio(treino, indice_aluno)
    elif opcao == 3:
        excluir_exercicio(treino, indice_aluno)
    elif opcao == 4:
        excluir_todos_exercicios(indice_aluno, treino)
    else:
        print("Opção inválida.")

# função de incluir exercício ao treino
def incluir_exercicio(indice_aluno):
    novo_exercicio = Exercicio()
    novo_exercicio.nome_exercicio = input("Nome do exercício: ")
    # verifica se o exercício já existe no treino
    for i in range(len(treinos[indice_aluno])):
        if novo_exercicio.nome_exercicio == treinos[indice_aluno][i].nome_exercicio:
            print("O exercício já existe no treino.")
            return
    novo_exercicio.peso_exercicio = input("Peso do exercício: ")
    novo_exercicio.num_repeticoes = input("Repetições do exercício: ")
    treinos[indice_aluno].append(novo_exercicio)
    # aluno passa a ser ativo no sistema
    alunos[indice_aluno].status = True

# função para alterar treinos já existentes
def alterar_exercicio(treino, indice_aluno):
    exercicio = input("Nome do exercício a ser alterado: ")

    for i in range(len(treinos[indice_aluno])):
        if exercicio == treinos[indice_aluno][i].nome_exercicio:
            novas_rep = int(input("Novo número de repetições: "))
            treinos[indice_aluno][i].num_repeticoes = novas_rep
            novo_peso = float(input("Novo peso utilizado: "))
            treinos[indice_aluno][i].peso_exercicio = novo_peso
            break
    else:
        print("Exercício não encontrado.")

# função para excluir treino
def excluir_exercicio(treino, indice_aluno):
    exercicio = input("Nome do exercício a ser excluído: ")

    # verificar se o exercício existe no treino
    for i in range(len(treinos[indice_aluno])):
        if exercicio == treinos[indice_aluno][i].nome_exercicio:
            treino.pop(indice_aluno)
            print("Exercício excluído.")
            break
    else:
        print("Exercício não encontrado.")

# função para excluir todos os treinos
def excluir_todos_exercicios(indice_aluno, treino):
    treino.clear()
    print("Exercícios excluídos!")
    # aluno passa a ser inativo no sistema
    alunos[indice_aluno].status = False

# funções de gereciamento de alunos
# função para buscar aluno na matriz
def buscar_aluno(nome):
    for i, aluno in enumerate(alunos):
        if aluno.nome == nome:
            return i
    return -1

# função para exibir o status do aluno
def exibir_status_aluno(aluno):
    if aluno.status == True:
        print("Status: Ativo")
    else:
        print("Status: Inativo")

# função do cálculo do imc
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")

# função de consultar aluno (opção 3 do menu principal)
def consultar_aluno():
    nome = input("Digite o nome do aluno: ")
    indice_aluno = buscar_aluno(nome)

    if indice_aluno == -1:
        print("Aluno não encontrado.")
        return

    aluno = alunos[indice_aluno]
    treino = treinos[indice_aluno]

    print("Dados do Aluno:")
    print("Nome:", aluno.nome)
    print("CPF:", aluno.cpf)
    print("Peso:", aluno.peso)
    print("Altura:", aluno.altura)
    exibir_status_aluno(aluno)
    calcular_imc(aluno.peso, aluno.altura)

    print("Treino:")
    print("{:<20} {:<10} {:<10}".format("Exercício", "Repetições", "Peso Utilizado"))
    for exercicio in treino:
        if exercicio:
            print("{:<20} {:<10} {:<10}".format(exercicio.nome_exercicio, exercicio.num_repeticoes, exercicio.peso_exercicio))

# função para atualizar cadastro já existente
def atualizar_cadastro_aluno(aluno):
    nome = input("Digite o nome do aluno: ")
    indice_aluno = buscar_aluno(nome)

    if indice_aluno == -1:
        print("Aluno não encontrado.")
        return

    aluno = alunos[indice_aluno]

    novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
    aluno.nome = novo_nome if novo_nome else aluno.nome

    novo_cpf = input("Novo CPF (deixe em branco para manter o mesmo): ")
    aluno.cpf = novo_cpf if novo_cpf else aluno.cpf

    novo_peso = input("Novo peso (deixe em branco para manter o mesmo): ")
    aluno.peso = float(novo_peso) if novo_peso else aluno.peso

    novo_altura = input("Nova altura (deixe em branco para manter o mesmo): ")
    aluno.altura = float(novo_altura) if novo_altura else aluno.altura

    print("Cadastro do aluno atualizado com sucesso!")

# função para excluir cadastro de aluno
def excluir_aluno():
    nome = input("Digite o nome do aluno: ")
    indice_aluno = buscar_aluno(nome)

    if indice_aluno == -1:
        print("Aluno não encontrado.")
        return

    aluno = alunos[indice_aluno]

    confirmacao = input(f"Tem certeza que deseja excluir o aluno {aluno.nome}? (S/N): ")

    if confirmacao.upper() == "S":
        alunos.pop(indice_aluno)
        treinos.pop(indice_aluno)
        print("Aluno excluído com sucesso!")

# função de relatório de alunos
def relatorio_alunos():
    print("Menu de Relatório de Alunos:")
    print("1 - Todos os alunos")
    print("2 - Alunos ativos")
    print("3 - Alunos inativos")
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        filtrar_alunos()
    elif opcao == 2:
        filtrar_alunos(True)
    elif opcao == 3:
        filtrar_alunos(False)
    else:
        print("Opção inválida.")

# função complementar para o relátorio de alunos, filtra os alunos por status no sistema
def filtrar_alunos(status=None):
    if status is None:
        alunos_filtrados = alunos
    else:
        alunos_filtrados = [aluno for aluno in alunos if aluno.status == status]

    if len(alunos_filtrados) == 0:
        print("Nenhum aluno encontrado.")
        return

    alunos_filtrados = sorted(alunos_filtrados, key=lambda x: x.nome)

    print("{:<20} {:<15} {:<10} {:<10}".format("Nome", "CPF", "Peso", "Altura"))
    for aluno in alunos_filtrados:
        print("{:<20} {:<15} {:<10} {:<10}".format(aluno.nome, aluno.cpf, aluno.peso, aluno.altura))

# menu principal
def menu():
    while True:
        print("\nMenu Principal:")
        print("1 - Cadastrar aluno")
        print("2 - Gerenciar treino")
        print("3 - Consultar aluno")
        print("4 - Atualizar cadastro do aluno")
        print("5 - Excluir aluno")
        print("6 - Relatório de alunos")
        print("0 - Sair")
        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            gerenciar_treino()
        elif opcao == 3:
            consultar_aluno()
        elif opcao == 4:
            atualizar_cadastro_aluno(alunos)
        elif opcao == 5:
            excluir_aluno()
        elif opcao == 6:
            relatorio_alunos()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Digite novamente.")

menu()
