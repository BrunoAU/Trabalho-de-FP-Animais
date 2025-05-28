import os, time

animais = []
eventos = []
metas = []
sugestoes_cuidados = []
lista_compras = []

ARQUIVO_DADOS = "dados_animais.txt"

def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        for animal in animais:
            f.write(f"ANIMAL|{animal['nome']}|{animal['especie']}|{animal['raca']}|{animal['idade']}|{animal['peso']}\n")
        for evento in eventos:
            f.write(f"EVENTO|{evento['titulo']}|{evento['data']}|{evento['descricao']}\n")
        for meta in metas:
            f.write(f"META|{meta['objetivo']}|{meta['prazo']}|{meta['status']}\n")
        for item in lista_compras:
            f.write(f"COMPRA|{item}\n")
def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        for linha in f:
            partes = linha.strip().split("|")
            tipo = partes[0]

            if tipo == "ANIMAL":
                animal = {
                    "nome": partes[1],
                    "especie": partes[2],
                    "raca": partes[3],
                    "idade": partes[4],
                    "peso": partes[5]
                }
                animais.append(animal)
            elif tipo == "EVENTO":
                evento = {
                    "titulo": partes[1],
                    "data": partes[2],
                    "descricao": partes[3]
                }
                eventos.append(evento)
            elif tipo == "META":
                meta = {
                    "objetivo": partes[1],
                    "prazo": partes[2],
                    "status": partes[3]
                }
                metas.append(meta)
            elif tipo == "COMPRA":
                lista_compras.append(partes[1])
def cadastrar_animal():
    print("\n--- Cadastro de Animal ---")
    nome = input("Nome do animal: ").strip()
    especie = input("Espécie: ").strip()
    raca = input("Raça: ").strip()
    idade = input("Data de nascimento (DD/MM/AAAA): ").strip()
    peso = input("Peso (kg): ").strip()
    os.system('cls')

    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "peso": peso
    }

    animais.append(animal)
    print(f"\nAnimal '{nome}' cadastrado com sucesso!")
def listar_animais():
    print("\n--- Lista de Animais ---")
    if not animais:
        print("Nenhum animal cadastrado.")
        time.sleep(1.5)
        os.system('cls')
    else:
        for i, animal in enumerate(animais, start=1):
            print(f"{i}. Nome: {animal['nome']}, Espécie: {animal['especie']}, Raça: {animal['raca']}, Data de nascimento: {animal['idade']}, Peso: {animal['peso']} kg")
def editar_animal():
    listar_animais()
    if not animais:
        return

    try:
        indice = int(input("\nDigite o número do animal que deseja editar: ")) - 1
        if 0 <= indice < len(animais):
            print("\nDeixe em branco para manter o valor atual.")
            animal = animais[indice]
            nome = input(f"Novo nome ({animal['nome']}): ").strip()
            especie = input(f"Nova espécie ({animal['especie']}): ").strip()
            raca = input(f"Nova raça ({animal['raca']}): ").strip()
            idade = input(f"Nova data de nascimento ({animal['idade']}): ").strip()
            peso = input(f"Novo peso ({animal['peso']}): ").strip()
            os.system('cls')

            if nome: animal["nome"] = nome
            if especie: animal["especie"] = especie
            if raca: animal["raca"] = raca
            if idade: animal["idade"] = idade
            if peso: animal["peso"] = peso

            print("\nAnimal atualizado com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
def remover_animal():
    listar_animais()
    if not animais:
        return

    try:
        indice = int(input("\nDigite o número do animal que deseja remover: ")) - 1
        os.system('cls')
        if 0 <= indice < len(animais):
            removido = animais.pop(indice)
            print(f"\nAnimal '{removido['nome']}' removido com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
def cadastrar_evento():
    print("\n--- Cadastro de Evento ---")
    titulo = input("Título do evento: ")
    data = input("Data (DD/MM/AAAA): ")
    descricao = input("Descrição: ")
    os.system('cls')

    evento = {"titulo": titulo, "data": data, "descricao": descricao}
    eventos.append(evento)
    print("Evento cadastrado com sucesso!")
def listar_eventos():
    print("\n--- Lista de Eventos ---")
    if not eventos:
        print("Nenhum evento cadastrado.")
        time.sleep(1.5)
        os.system('cls')
    else:
        for i, evento in enumerate(eventos, start=1):
            print(f"{i}. {evento['titulo']} - Data: {evento['data']} - Descrição: {evento['descricao']}")
def concluir_eventos():
    try:
        print("\n--- Concluir Eventos ---")
        if not eventos:
            print("Não há eventos a serem concluídos.")
            time.sleep(1.5)
            os.system('cls')
        else:
            for i, evento in enumerate(eventos, start=1):
                print(f"{i}. {evento['titulo']} - Data: {evento['data']} - Descrição: {evento['descricao']}")
            conc_eventos = int(input("Qual evento você deseja concluir? "))
            os.system('cls')
            if 1 <= conc_eventos <= len(eventos):
                eventos.pop(conc_eventos-1)
                print("Evento concluído!")
    except ValueError:
        print("Opção inválida, por favor, insira um número inteiro")                 
def cadastrar_meta():
    print("--- Cadastro de Meta ---")
    objetivo = input("Objetivo: ")
    prazo = input("Prazo (DD/MM/AAAA): ")
    os.system('cls')

    meta = {"objetivo": objetivo, "prazo": prazo}
    metas.append(meta)
    print("Meta cadastrada com sucesso!")
def listar_metas():
    print("--- Lista de Metas ---")
    if not metas:
        print("Nenhuma meta cadastrada.")
        time.sleep(1.5)
        os.system('cls')
    else:
        for i, meta in enumerate(metas, start=1):
            print(f"{i}. {meta['objetivo']} - Prazo: {meta['prazo']}")
def concluir_metas():
    try:
        print("--- Concluir Metas ---")
        if not metas:
            print("Não há metas a serem concluídas.")
            time.sleep(1.5)
            os.system('cls')
        else:
            for i, meta in enumerate(metas, start=1):
                print(f"{i}. {meta['objetivo']} - Prazo: {meta['prazo']}")
            conc_metas = int(input("Qual meta você deseja concluir? "))
            os.system('cls')
            if 1 <= conc_metas <= len(metas):
                metas.pop(conc_metas-1)
                print("Meta concluída!")
    except ValueError:
        print("Opção inválida, por favor, insira um número inteiro")
def adicionar_item_compra():
    item = input("Digite o item para adicionar à lista de compras: ").strip()
    os.system('cls')
    if item:
        lista_compras.append(item)
        print(f"Item '{item}' adicionado com sucesso.")
    else:
        print("Item vazio não pode ser adicionado.")
def listar_compras():
    print("--- Lista de Compras ---")
    if not lista_compras:
        print("Nenhum item na lista de compras.")
        time.sleep(1.5)
        os.system('cls')
    else:
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
def remover_compras():
    print("--- Remover Itens da Lista de Compras ---")
    if not lista_compras:
        print("Nenhum item na lista de compras.")
        time.sleep(1.5)
        os.system('cls')
    else:
        try:
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
            indice = int(input("\nDigite o número da compra que deseja remover: ")) - 1
            os.system('cls')
            if 0 <= indice < len(lista_compras):
                lista_compras.pop(indice)
                print(f"Item removido!")
            else:
                print("Número inválido.")
        except ValueError:
            os.system('cls')
            print("Entrada inválida. Digite um número.")
def sugerir_cuidados():
    while True:
        try:
            esc_cuidados = int(input("\n1: Cachorro\n2: Gato\n3: Voltar\nPara qual animal você deseja sugestões de cuidados? "))
            os.system('cls')
            if esc_cuidados == 1:
                idade = int(input("1: Adulto\n2: Filhote\nQual a idade do seu animal? "))
                os.system('cls')
                if idade == 1:
                    cuidados_cachorro = int(input("1: Cuidados principais\n2: Cuidados de higiene\n3: Cuidados de "
                    "bem-estar e comportamento\n4: Saúde\n5: Amor e atenção\nEscolha sua opção: "))
                    os.system('cls')
                    if cuidados_cachorro == 1:
                        print("Cuidados principais:\n1: Alimentação balanceada: Escolha uma ração de qualidade, adequada à idade,"
                        " porte e condição de saúde do cão.\n2: Água fresca sempre disponível: Troque a água com frequência e "
                        "mantenha o pote limpo.\n3: Vacinação em dia: Previna doenças com as vacinas obrigatórias e reforços "
                        "anuais.\n4: Vermifugação regular: Siga a recomendação do veterinário para manter o cão livre de vermes."
                        "\n5: Controle de pulgas e carrapatos: Use produtos indicados e inspecione o pelo com frequência.")
                    elif cuidados_cachorro == 2:
                        print("Cuidados de higiene:\n1: Banho regular: A cada 15 dias ou conforme a raça e estilo de vida.\n2: Escovação "
                        "dos pelos: Ajuda a remover pelos mortos e evita nós (principalmente em cães de pelo longo).\n3: Higiene"
                        " bucal: Escove os dentes com produtos próprios para cães.\n4: Corte das unhas: Deve ser feito com cuidado"
                        " para não machucar.")
                    elif cuidados_cachorro == 3:
                        print("Cuidados de bem-estar e comportamento:\n1: Passeios diários: Importantes "                        
                        "para saúde física e mental.\n2: Brincadeiras e estímulo mental: Use brinquedos "
                        "interativos, petiscos escondidos, jogos de olfato.\n3: Socialização: Deixe o cão "
                        "conviver com outros cães e pessoas desde filhote, se possível.\n4: Treinamento com "
                        "reforço positivo: Ensina comandos e fortalece a relação tutor-cão.")
                    elif cuidados_cachorro == 4:
                        print("Cuidados de saúde:\n1: Visitas regulares ao veterinário: Para check-ups, "
                        "vacinas e qualquer sinal de problema.\n2: Atenção a sinais de dor ou desconforto: "
                        "Mudanças de comportamento, apatia, coceira ou mancar podem ser sintomas importantes.")
                    elif cuidados_cachorro == 5:
                        print("Cuidados de saúde:\n1: Demonstre carinho diariamente: Cães precisam de afeto"
                        " tanto quanto de comida.\n2: Proporcione um espaço seguro e confortável: Uma "
                        "caminha limpa, longe de correntes de ar e ruídos.")
                    else:
                        print("Opção inválida")
                        time.sleep(1.5)
                        os.system('cls')
                elif idade == 2:
                    cuidados_cachorro = int(input("\n1: Cuidados principais\n2: Cuidados de higiene\n3: Cuidados de "
                    "Comportamento e socialização\n4: Saúde\n5: Estímulo e aprendizado\n6: Alimentação\nEscolha sua opção: "))
                    os.system('cls')
                    if cuidados_cachorro == 1:
                        print("Cuidados principais:\n1:Vacinação e vermifugação em dia: Protege "
                        "contra doenças sérias logo nos primeiros meses.\n2: Alimentação adequada para"
                        " filhotes: Rações específicas garantem crescimento saudável.\n3: Socialização"
                        " e carinho diário: Ajuda no desenvolvimento emocional e evita comportamentos"
                        " agressivos ou medrosos.")
                    elif cuidados_cachorro == 2:
                        print("Cuidados de higiene:\n1: Banho só após as primeiras vacinas: Para evitar doenças."
                        "\n2: Limpeza delicada de olhos, orelhas e patas: Com panos ou produtos específicos."
                        "\n3: Caminha sempre limpa: Para evitar infecções.")
                    elif cuidados_cachorro == 3:
                        print("Cuidados de Comportamento e socialização:\n1: Socialização gradual: "
                        "Após o ciclo de vacinas.\n2: Ensinar o local do xixi: Com paciência e rotina."
                        "\n3: Brinquedos para morder: Aliviam o desconforto da dentição.")
                    elif cuidados_cachorro == 4:
                        print("Cuidados de saúde:\n1: Vacinação completa: Começa a partir das 6 semanas."
                        "\n2: Vermifugação correta: Inicia aos 15-30 dias de vida.\n3: Primeira "
                        "consulta veterinária: Assim que o filhote chegar em casa.")
                    elif cuidados_cachorro == 5:
                        print("Cuidados de estímulo e aprendizado:\n1: Começar o treinamento básico"
                        " cedo: Com reforço positivo.\n2: Brincadeiras educativas: Estimulam o cérebro."
                        "\n3: Rotina consistente: Dá segurança e evita ansiedade.")
                    elif cuidados_cachorro == 6:
                        print("Cuidados com a alimentação:\n1: Ração específica para filhotes: Rica em"
                        " nutrientes para o crescimento.\n2: Nada de comida humana: Pode ser perigosa."
                        "\n3: Horários fixos: Ajuda na digestão e disciplina.")
                    else:
                        print("Opção inválida")
                        time.sleep(1.5)
                        os.system('cls')
                else:
                    print("\nOpção inválida")
                    time.sleep(1.5)
                    os.system('cls')
            elif esc_cuidados == 2:
                idade = int(input("1: Adulto\n2: Filhote\nQual a idade do seu animal? "))
                os.system('cls')
                if idade == 1:
                    cuidados_gato = int(input("\n1: Cuidados principais\n2: Cuidados de higiene\n3: Cuidados de segurança\n4: "
                    "Cuidados de atenção e vínculo\n5: Cuidados de estímulo e comportamento\nEscolha sua opção: "))
                    os.system('cls')
                    if cuidados_gato == 1:
                        print("Cuidados principais:\n1: Alimentação adequada: Ração de qualidade e água fresca sempre disponível"
                        "\n2: Caixa de areia limpa: Limpe todos os dias\n3: Vacinação e vermífugo em dia:"
                        " Visitas regulares ao veterinário.\n4: Castração: Ajuda na saúde e comportamento.")
                    elif cuidados_gato == 2:
                        print("Cuidados de higiene:\n1: Caixa de areia limpa: Limpar todos os dias e trocar a areia regularmente."
                        "\n2: Escovação dos pelos: Especialmente para gatos de pelo longo.\n3: Corte das unhas: Regular, com "
                        "cuidado para não cortar muito rente.")
                    elif cuidados_gato == 3:
                        print("Cuidados de segurança:\n1: Ambiente seguro e protegido: Telas nas janelas para gatos que vivem "
                        "em apartamento.\n2: Evite plantas tóxicas: Como lírios, comigo-ninguém-pode, entre outras.\n3: " 
                        "Supervisão ao sair de casa: Se for sair, que seja com guia apropriada e com supervisão.")
                    elif cuidados_gato == 4:
                        print("Cuidados de atenção e vínculo:\n1: Respeitar o tempo do gato: Nem sempre ele quer colo, mas ama a"
                        " companhia.\n2: Consultas veterinárias regulares: Mesmo sem sinais de doença, o check-up é importante."
                        "\n3: Muito amor e paciência: Gatos são independentes, mas criam laços fortes com quem os respeita.")
                    elif cuidados_gato == 5:
                        print("Cuidados de estímulo e comportamento:\n1: Arranhadores disponíveis: Evita que arranhem móveis e "
                        "ajuda a desgastar as unhas.\n2: Brinquedos interativos: Enriquecem o ambiente e evitam o tédio.\n3: " 
                        "Lugar seguro para descanso: Gatos gostam de tocas, prateleiras e lugares altos.")
                    else:
                        print("Opção inválida")
                        time.sleep(1.5)
                        os.system('cls')
                elif idade == 2:
                    cuidados_gato = int(input("\n1: Cuidados principais\n2: Cuidados de higiene\n3: Cuidados de saúde\n4: Cuidados"
                    " de alimentação\n5: Cuidados de estímulo e comportamento\n6: Segurança e conforto\nEscolha sua opção: "))
                    os.system('cls')
                    if cuidados_gato == 1:
                        print("Cuidados principais:\n1: Vacinação e vermifugação em dia: Protege contra doenças perigosas logo no"
                        " início da vida.\n2: Alimentação adequada para filhotes: Garante crescimento saudável e forte.\n3: "
                        "Ambiente seguro e estímulos positivos: Telas de proteção, brinquedos e socialização ajudam no "
                        "desenvolvimento físico e emocional.")
                    elif cuidados_gato == 2:
                        print("Cuiados de higiene:\n1: Caixa de areia adequada: De fácil acesso e sempre limpa.\n2: Escovação"
                        "dos pelos: Desde pequeno, para acostumar.\n3: Cuidados com olhos, orelhas e unhas: Limpeza suave e "
                        "cortes regulares.")
                    elif cuidados_gato == 3:
                        print("Cuidados de saúde:\n1: Vacinação completa: Começa por volta de 2 meses de vida.\n2: Vermifugação"
                        " regular: Elimina parasitas internos.\n3: Consultas veterinárias periódicas: Para acompanhar o crescimento"
                        " e prevenir doenças.")
                    elif cuidados_gato == 4:
                        print("Cuidados de alimentação:\n1: Ração específica para filhotes: Rica em nutrientes para o "
                        "desenvolvimento.\n2: Água sempre limpa e fresca: Fundamental para a saúde dos rins.\n3: Nada de leite de"
                        " vaca: Pode causar problemas digestivos.")
                    elif cuidados_gato == 5:
                        print("Cuidados de estímulo e comportamento:\n1: Socialização precoce: Para ser um gato mais amigável e"
                        " confiante.\n2: Brinquedos apropriados: Estimulam o instinto de caça e evitam o tédio.\n3: Arranhadores:"
                        " Ensinar a usar desde filhote para preservar móveis e cuidar das unhas.")
                    elif cuidados_gato == 6:
                        print("Cuidados de segurança e conforto:\n1: Ambiente seguro: Telas de proteção nas janelas e nada de "
                        "passeios sem supervisão.\n2: Caminha confortável: Em um local tranquilo e protegido.\n3: Rotina estável:"
                        " Alimentação, brincadeiras e descanso em horários parecidos ajudam na adaptação.")
                    else:
                        print("Opção inválida")
                        time.sleep(1.5)
                        os.system('cls')
            elif esc_cuidados == 3:
                break
            else:
                print("Opção inválida")
                time.sleep(1.5)
                os.system('cls')
        except ValueError:
            os.system('cls')
            print("Entrada inválida. Digite um número.")
            time.sleep(1.5)
            os.system('cls')
def menu_crud_animais():
    while True:
        print("\n=== Menu de Animais ===")
        print("1. Cadastrar Animal")
        print("2. Listar Animais")
        print("3. Editar Animal")
        print("4. Remover Animal")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        os.system('cls')
        if opcao == "1":
            cadastrar_animal()
        elif opcao == "2":
            listar_animais()
        elif opcao == "3":
            editar_animal()
        elif opcao == "4":
            remover_animal()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")
            time.sleep(1.5)
            os.system('cls')
def menu_eventos():
    while True:
        print("\n=== Menu de Eventos ===")
        print("1. Cadastrar Evento")
        print("2. Listar Eventos")
        print("3. Concluir Evento")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        os.system('cls')
        if opcao == "1":
            cadastrar_evento()
        elif opcao == "2":
            listar_eventos()
        elif opcao == "3":
            concluir_eventos()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
            time.sleep(1.5)
            os.system('cls')
def menu_metas():
    while True:
        print("\n=== Menu de Metas ===")
        print("1. Cadastrar Meta")
        print("2. Listar Metas")
        print("3. Concluir metas")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        os.system('cls')
        if opcao == "1":
            cadastrar_meta()
        elif opcao == "2":
            listar_metas()
        elif opcao == "3":
            concluir_metas()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
            time.sleep(1.5)
            os.system('cls')
def menu_compras():
    while True:
        print("\n=== Menu de Lista de Compras ===")
        print("1. Adicionar Item")
        print("2. Listar Itens")
        print("3. Excluir Item")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        os.system('cls')
        if opcao == "1":
            adicionar_item_compra()
        elif opcao == "2":
            listar_compras()
        elif opcao == "3":
            remover_compras()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
            time.sleep(1.5)
            os.system('cls')
def menu_principal():
    carregar_dados()
    while True:
        print("\n\033[1;32m====== SISTEMA DE GERENCIAMENTO DE CUIDADOS COM ANIMAIS ======\033[1;37m")
        print("1. Gerenciar Animais")
        print("2. Gerenciar Eventos")
        print("3. Gerenciar Metas")
        print("4. Sugestões de Cuidados")
        print("5. Lista de Compras")
        print("6. Salvar & sair")

        opcao = input("\033[1;90mEscolha uma opção: \033[0;37m").strip()
        os.system('cls')
        if opcao == "1":
            menu_crud_animais()
        elif opcao == "2":
            menu_eventos()
        elif opcao == "3":
            menu_metas()
        elif opcao == "4":
            sugerir_cuidados()
        elif opcao == "5":
            menu_compras()
        elif opcao == "6":
            salvar_dados()
            print("Encerrando o programa. Até logo!")
            time.sleep(1.5)
            os.system('cls')
            break
        else:
            print("\033[1;31mOpção inválida...")
            time.sleep(0.3)
            os.system('cls')
def logo():
    os.system('cls')
    ascii_art = [
    "\033[37m██\033[90m╗   \033[37m██\033[90m╗\033[37m██\033[90m╗\033[37m██████\033[90m╗  \033[37m█████\033[90m╗     \033[37m██████\033[90m╗ \033[37m███████\033[90m╗\033[37m████████\033[90m╗",
    "\033[37m██\033[90m║   \033[37m██\033[90m║\033[37m██\033[90m║\033[37m██\033[90m╔══\033[37m██\033[90m╗\033[37m██\033[90m╔══\033[37m██\033[90m╗    \033[37m██\033[90m╔══\033[37m██\033[90m╗\033[37m██\033[90m╔════╝╚══\033[37m██\033[90m╔══╝",
    "\033[37m██\033[90m║   \033[37m██\033[90m║\033[37m██\033[90m║\033[37m██\033[90m║  \033[37m██\033[90m║\033[37m███████\033[90m║    \033[37m██████\033[90m╔╝\033[37m█████\033[90m╗     \033[37m██\033[90m║",
    "\033[90m╚\033[37m██\033[90m╗ \033[37m██\033[90m╔╝\033[37m██\033[90m║\033[37m██\033[90m║  \033[37m██\033[90m║\033[37m██\033[90m╔══\033[37m██\033[90m║    \033[37m██\033[90m╔═══╝ \033[37m██\033[90m╔══╝     \033[37m██\033[90m║",
    "\033[90m ╚\033[37m████\033[90m╔╝ \033[37m██\033[90m║\033[37m██████\033[90m╔╝\033[37m██\033[90m║  \033[37m██\033[90m║    \033[37m██\033[90m║     \033[37m███████\033[90m╗   \033[37m██\033[90m║",
    "\033[90m  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝   ╚═╝",
    "\033[37m════════════════════════════════════════════════════════",
    "   Copyright   ©   1999-2025   VidaPet FPCC & Co. KG"
]
    for line in ascii_art:
        print(line)
        time.sleep(0.5)
    os.system('cls')
def logo_animada():
    frames = [
        [
            "\033[37m██\033[90m╗   \033[37m██\033[90m╗\033[37m██\033[90m╗\033[37m██████\033[90m╗  \033[37m█████\033[90m╗     \033[37m██████\033[90m╗ \033[37m███████\033[90m╗\033[37m████████\033[90m╗",
            "\033[37m██\033[90m║   \033[37m██\033[90m║\033[37m██\033[90m║\033[37m██\033[90m╔══\033[37m██\033[90m╗\033[37m██\033[90m╔══\033[37m██\033[90m╗    \033[37m██\033[90m╔══\033[37m██\033[90m╗\033[37m██\033[90m╔════╝╚══\033[37m██\033[90m╔══╝",
            "\033[37m██\033[90m║   \033[37m██\033[90m║\033[37m██\033[90m║\033[37m██\033[90m║  \033[37m██\033[90m║\033[37m███████\033[90m║    \033[37m██████\033[90m╔╝\033[37m█████\033[90m╗     \033[37m██\033[90m║",
            "\033[90m╚\033[37m██\033[90m╗ \033[37m██\033[90m╔╝\033[37m██\033[90m║\033[37m██\033[90m║  \033[37m██\033[90m║\033[37m██\033[90m╔══\033[37m██\033[90m║    \033[37m██\033[90m╔═══╝ \033[37m██\033[90m╔══╝     \033[37m██\033[90m║",
            "\033[90m ╚\033[37m████\033[90m╔╝ \033[37m██\033[90m║\033[37m██████\033[90m╔╝\033[37m██\033[90m║  \033[37m██\033[90m║    \033[37m██\033[90m║     \033[37m███████\033[90m╗   \033[37m██\033[90m║",
            "\033[90m  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝   ╚═╝"
        ],
        [
            "\033[30m██\033[37m╗   \033[30m██\033[37m╗\033[30m██\033[37m╗\033[30m██████\033[37m╗  \033[30m█████\033[37m╗     \033[30m██████\033[37m╗ \033[30m███████\033[37m╗\033[30m████████\033[37m╗",
            "\033[30m██\033[37m║   \033[30m██\033[37m║\033[30m██\033[37m║\033[30m██\033[37m╔══\033[30m██\033[37m╗\033[30m██\033[37m╔══\033[30m██\033[37m╗    \033[30m██\033[37m╔══\033[30m██\033[37m╗\033[30m██\033[37m╔════╝╚══\033[30m██\033[37m╔══╝",
            "\033[30m██\033[37m║   \033[30m██\033[37m║\033[30m██\033[37m║\033[30m██\033[37m║  \033[30m██\033[37m║\033[30m███████\033[37m║    \033[30m██████\033[37m╔╝\033[30m█████\033[37m╗     \033[30m██\033[37m║",
            "\033[37m╚\033[30m██\033[37m╗ \033[30m██\033[37m╔╝\033[30m██\033[37m║\033[30m██\033[37m║  \033[30m██\033[37m║\033[30m██\033[37m╔══\033[30m██\033[37m║    \033[30m██\033[37m╔═══╝ \033[30m██\033[37m╔══╝     \033[30m██\033[37m║",
            "\033[37m ╚\033[30m████\033[37m╔╝ \033[30m██\033[37m║\033[30m██████\033[37m╔╝\033[30m██\033[37m║  \033[30m██\033[37m║    \033[30m██\033[37m║     \033[30m███████\033[37m╗   \033[30m██\033[37m║",
            "\033[37m  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝   ╚═╝"
        ]
    ]

    footer = [
        "\033[37m════════════════════════════════════════════════════════",
        "   Copyright   ©   1999-2025   VidaPet FPCC & Co. KG"
    ]


    while True:
        for _ in range(4):
            for frame in frames:
                os.system('cls' if os.name == 'nt' else 'clear')
                for line in frame:
                    print(line)
                for line in footer:
                    print(line)
                time.sleep(0.5)
        break
    os.system('cls')

logo()
logo_animada()
menu_principal()