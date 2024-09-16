catalogo = []

def menu():
    def inicio(): # Função que dá início ao programa com a mensagem de boas-vindas e opções para iniciar ou sair.
        print("-" * 75)
        print("." * 3, "Bem-vindo(a) à PyFlix!", "." * 3)
        print("-" * 75)

        while True:
            print("Deseja iniciar o programa?")
            print("s - Sim | n - Não")
            print("-" * 75)

            iniciar = input("Sim ou Não? ").strip().lower() # Solicita a resposta do usuário e normaliza para minúsculas.

            if iniciar == 's':
                print("Carregando...")
                return True # Retorna True para iniciar o programa.
            elif iniciar == 'n':
                print("Tudo bem...Tchau!")
                return False # Retorna False para sair do programa.
            else:
                print("Resposta inválida! Tente novamente:")
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                print("-" * 75)

    def funcionalidades(): # Função que exibe as opções disponíveis para o usuário e coleta a escolha.
        while True:
            print("-" * 75)
            print("O que deseja?")
            print("1 - Adicionar filme")
            print("2 - Listar filmes")
            print("3 - Buscar filme por título")
            print("4 - Atualizar filme")
            print("5 - Remover filme")
            print("6 - Sair")
            print("-" * 75)

            print("." * 5, "Escolha uma opção!", "." * 5)   
            print("-" * 75)

            opcao = input("Opção: ").strip() # Solicita a opção do usuário.

            if opcao in ['1', '2', '3', '4', '5', '6']:
                return opcao # Retorna a opção selecionada.
            else:
                print("Opção inválida! Tente novamente:")
    
    if inicio(): # Se a função inicio() retorna True (usuário deseja iniciar o programa).
        while True:
            escolha = funcionalidades() # Coleta a escolha do usuário.
            if escolha == '1':
                adicionar() # Chama a função para adicionar um filme.
            elif escolha == '6':
                print("Saindo...")
                break # Encerra o loop e, consequentemente, o programa.
            elif catalogo: # Verifica se o catálogo de filmes não está vazio.
                if escolha == '2':
                    listar() # Chama a função para listar filmes.
                elif escolha == '3':
                    buscar() # Chama a função para buscar um filme.
                elif escolha == '4':
                    atualizar() # Chama a função para atualizar um filme.
                elif escolha == '5':
                    remover() # Chama a função para remover um filme.
            else: # Se o catálogo estiver vazio.
                print("O catálogo está vazio!")
                print("Adicione algum filme antes de usar esta opção.")

def tratar_acentos(texto): # Função para processar o texto, removendo caracteres acentuados e substituindo-os por suas versões não acentuadas.
    acentuados = 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'
    sem_acento = 'aaaaeeiooouucAAAAEEIOOOUUC' # String com os caracteres correspondentes sem acento, na mesma ordem.
    
    texto_sem_acento = ""
    
    for caractere in texto: 
        if caractere in acentuados: # Verifica se o caractere atual está na string de caracteres acentuados.
            indice = acentuados.index(caractere)  # Encontra o índice do caractere acentuado na string 'acentuados'.
            texto_sem_acento += sem_acento[indice] # Usa o índice para encontrar o caractere correspondente sem acento na string 'sem_acento'.
        else:
            texto_sem_acento += caractere # Se o caractere não é acentuado, adiciona-o diretamente ao texto resultante.
    
    return texto_sem_acento # Retorna o texto com os acentos removidos.

def adicionar(): # Função para coletar e validar informações sobre um filme e adicioná-lo ao catálogo.
    print("-" * 75)
    print("." * 3, "Informe as seguintes informações do filme que você deseja adicionar", "." * 3)
    print("-" * 75)
    
    titulo = input("Título: ").strip().capitalize() # Solicita o título do filme e capitaliza a primeira letra.
    while not titulo:  # Verifica se o título não está vazio; caso esteja, solicita novamente.
        print("Título vazio!")
        print("Por favor, insira o título do filme:")
        titulo = input("Título: ").strip().capitalize()

    diretor_a = input("Diretor(a): ").strip().capitalize() # Solicita o nome do diretor e capitaliza a primeira letra.
    while not diretor_a or diretor_a.isdigit() or diretor_a in '"!¹1/2²@?°3³#$4£5%¢6¨¬7&8*9()0-_=+§`´{}ª[]º^~<,>;:|\/*': # Verifica se o nome do diretor não está vazio, não contém apenas dígitos e não possui caracteres inválidos.
        if diretor_a == "":
            print("Diretor(a) não informado!")
            print("Informe para prosseguirmos:")
        elif diretor_a.isdigit():
            print("Erro!")
            print("O nome do diretor deve conter apenas letras")
            print("e não dígitos numéricos.")
            print("Informe corretamente, por favor:")
        else:
            print("Erro!")
            print("O nome do diretor deve conter apenas letras")
            print("e não os demais caracteres.")
            print("Informe corretamente, por favor:")
        diretor_a = input("Diretor(a): ").strip().capitalize()

    ano_lancamento = input("Ano de lançamento: ").strip() # Solicita o ano de lançamento e remove espaços em branco ao redor.
    while not ano_lancamento or not ano_lancamento.isdigit() or not (1888 <= int(ano_lancamento) <= 2024):  # Verifica se o ano de lançamento está vazio, não é numérico ou não está entre 1888 e 2024.
        if ano_lancamento == "":
            print("Ano de lançamento vazio!")
            print("Insira, por favor:")
        elif not ano_lancamento.isdigit():
            print("Erro!")
            print("O ano de lançamento não pode ser um decimal,")
            print("nem conter letras ou demais caracteres.")
            print("Por favor, informe o ano corretamente:")
        else:
            print("Ano inválido!")
            print("Por favor, digite um ano entre 1888 e 2024")
        ano_lancamento = input("Ano de lançamento: ").strip()
    
    genero = input("Gênero: ").strip().lower() # Solicita o gênero do filme e transforma em minúsculas.
    while not genero or not genero.isalpha(): # Verifica se o gênero não está vazio e contém apenas letras.
        if genero == "":
            print("O Gênero não foi informado.")
            print("Insira, por favor:")
        else:
            print("O gênero deve conter apenas letras.")
            print("Não deve apresentar dígitos numéricos ou demais caracteres.")
            print("Por favor, informe o gênero do filme corretamente:")
        genero = input("Gênero: ").strip().lower()

    print("-" * 75)

    novo_filme = [titulo, diretor_a, ano_lancamento, genero] # Cria uma lista com as informações do novo filme.
    catalogo.append(novo_filme) # Adiciona a lista com o novo filme ao catálogo.
    print(f"O filme '{titulo}' foi adicionado com sucesso!")

    print("-" * 75)

def listar(): # Função permite ao usuário listar filmes do catálogo com base em critérios especificados.
    print("-" * 75)
    print("." * 2, "Seu catálogo de filmes:", "." * 2)
    print("-" * 75)
    
    while True:  # Loop que permite múltiplas buscas até que o usuário decida encerrar.
        while True: # Loop para garantir que o usuário escolha um critério válido para listar os filmes.
            print("-" * 75)
            print("Qual critério deseja utilizar para listar os filmes?")
            print("1 - Título")
            print("2 - Diretor(a)")
            print("3 - Ano")
            print("4 - Gênero")
            print("5 - Listar todos os filmes")
            print("-" * 75)

            opcao = input("Opção: ").strip() # Solicita ao usuário a escolha do critério e remove espaços em branco.
            print("-" * 75)

            if opcao in ['1', '2', '3', '4', '5']:
                if opcao == '1': # Define o critério com base na opção escolhida.
                    indice_criterio = 0
                    criterio = 'Título'
                elif opcao == '2':
                    indice_criterio = 1
                    criterio = 'Diretor(a)'
                elif opcao == '3':
                    indice_criterio = 2
                    criterio = 'Ano de Lançamento'
                elif opcao == '4':
                    indice_criterio = 3
                    criterio = 'Gênero'
                elif opcao == '5':
                    opcao = '5'
                break
            else:
                print("Opção inválida! Tente novamente.")
                print("-" * 75)

        filmes_filtrados = [] # Lista para armazenar os filmes que atendem ao critério.

        while True: # Loop para aplicar o filtro e buscar os filmes.
            if opcao == '5':
                filmes_filtrados = catalogo # Se a opção for '5', lista todos os filmes.
                break # Sai do loop após definir todos os filmes como filtrados.
            else:
                print(f"Insira o/a {criterio} que deseja usar como filtro: ")
                filtro = input(f"{criterio}: ").strip() # Solicita o critério de filtro do usuário.

                if filtro: # Verifica se o filtro não está vazio e aplica as validações apropriadas.
                    if opcao == '1': # Se o critério for 'Título'.
                        if not filtro: # Verifica se o filtro não está vazio.
                            print("Título vazio!")
                            print("Por favor, insira o título do filme:")
                        else:
                            for filme in catalogo:
                                if filtro.lower() in tratar_acentos(filme[indice_criterio]).lower(): # Verifica se o filtro está presente no campo especificado do filme, ignorando maiúsculas/minúsculas e acentos.
                                    filmes_filtrados.append(filme) # Adiciona o filme à lista de filmes filtrados se corresponder ao critério.
                        break # Sai do loop de filtragem após ter adicionado os filmes correspondentes à lista.
                    elif opcao == '2': # Se o critério for 'Diretor(a)'.
                        if not filtro: # Verifica se o título não está vazio.
                            print("Diretor(a) não informado!")
                            print("Informe para prosseguirmos:")
                        elif filtro.isdigit(): # Verifica se o filtro não contém apenas dígitos.
                            print("Erro!")
                            print("O nome do diretor deve conter apenas letras")
                            print("e não dígitos numéricos.")
                            print("Informe corretamente, por favor:")
                        elif filtro in '"!¹1/2²@?°3³#$4£5%¢6¨¬7&8*9()0-_=+§`´{}ª[]º^~<,>;:|\/*': # Verifica se o filtro não possui caracteres inválidos.
                            print("Erro!")
                            print("O nome do diretor deve conter apenas letras")
                            print("e não os demais caracteres.")
                            print("Informe corretamente, por favor:")
                        else:
                            for filme in catalogo:
                                if filtro.lower() in tratar_acentos(filme[indice_criterio]).lower(): # Verifica se o filtro está presente no campo especificado do filme, ignorando maiúsculas/minúsculas e acentos.
                                    filmes_filtrados.append(filme) # Adiciona o filme à lista de filmes filtrados se corresponder ao critério.
                        break # Sai do loop de filtragem após ter adicionado os filmes correspondentes à lista.
                    elif opcao == '3': # Se o critério for 'Ano de Lançamento'.
                        if not filtro: # Verifica se o filtro não está vazio.
                            print("Ano de lançamento vazio!")
                            print("Insira, por favor:")
                        elif not filtro.isdigit(): # Verifica se o filtro não é numérico.
                            print("Erro!")
                            print("O ano de lançamento não pode ser um decimal,")
                            print("nem conter letras ou demias caracteres.")
                            print("Por favor, informe o ano corretamente:")
                        elif not (1888 <= int(filtro) <= 2024): # Verifica se o filtro não está entre 1888 e 2024.
                            print("Ano inválido!")
                            print("Por favor, digite um ano entre 1888 e 2024")
                        else:
                            for filme in catalogo:
                                if filtro.lower() in tratar_acentos(filme[indice_criterio]).lower(): # Verifica se o filtro está presente no campo especificado do filme, ignorando maiúsculas/minúsculas e acentos.
                                    filmes_filtrados.append(filme) # Adiciona o filme à lista de filmes filtrados se corresponder ao critério.
                        break # Sai do loop de filtragem após ter adicionado os filmes correspondentes à lista.
                    elif opcao == '4': # Se o critério for 'Gênero'.
                        if not filtro: # Verifica se o filtro não está vazio.
                            print("O Gênero não foi informado.")
                            print("Insira, por favor:")
                        elif not filtro.isalpha(): # Verifica se o filtro contém apenas letras.
                            print("O gênero deve conter apenas letras.")
                            print("Não deve apresentar dígitos numéricos ou demais caracteres.")
                            print("Por favor, informe o gênero do filme corretamente:")
                        else:
                            for filme in catalogo:
                                if filtro.lower() in tratar_acentos(filme[indice_criterio]).lower(): # Verifica se o filtro está presente no campo especificado do filme, ignorando maiúsculas/minúsculas e acentos.
                                    filmes_filtrados.append(filme)  # Adiciona o filme à lista de filmes filtrados se corresponder ao critério.
                        break # Sai do loop de filtragem após ter adicionado os filmes correspondentes à lista.
                else:
                    print(f"Filtro vazio. Por favor, selecione um/a {criterio}.")
                    print("-" * 75)

        if filmes_filtrados: # Verifica se algum filme foi encontrado com o critério fornecido.
            cont = 1
            print("-" * 75)
            for filme in filmes_filtrados: # Mostra os filmes filtrados para o usuário.
                print(f"Filme {cont}:")
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)
                cont += 1
            break # Sai do loop de listagem após ter exibido todos os filmes filtrados.
        else: # Se a lista de filmes filtrados estiver vazia.
            print("Nenhum filme encontrado com esse critério.")
            print("-" * 75)
            while True: # Loop para perguntar ao usuário se deseja realizar uma nova busca.
                print("Deseja tentar uma nova busca com critérios diferentes?")
                print("s - Sim | n - Não")
                print("-" * 75)

                tentar_novamente = input("Sim ou Não? ").strip().lower() # Solicita ao usuário a resposta e a normaliza para minúsculas.
                if tentar_novamente == 's': # Se o usuário optar por sim, o loop de busca será reiniciado.
                    break 
                elif tentar_novamente == 'n': # Se o usuário optar por não, encerra a função de listagem.
                    print("Encerrando a listagem...")
                    return
                else: # Se a resposta não for válida, solicita que o usuário tente novamente.
                    print("Resposta inválida! Tente novamente:")
                    print("Por favor, digite 's' para Sim ou 'n' para Não.")
                    print("-" * 75)

def buscar():  # Função que permite ao usuário procurar filmes no catálogo pelo título.
    print("-" * 75)
    print("." * 2, "Por qual filme você busca?", "." * 2)
    print("-" * 75)

    while True: # Loop que permite ao usuário buscar filmes repetidamente.
        titulo_buscado = input("Título do filme buscado: ").strip() # Solicita ao usuário o título do filme e remove espaços em branco.

        titulo_buscado = tratar_acentos(titulo_buscado).lower() # Remove acentos e converte o título para minúsculas para facilitar a comparação.
        print("-" * 75)

        while not titulo_buscado: # Verifica se o título buscado está vazio.
            print("Título vazio! Por favor, insira o título do filme que você deseja buscar:")
            titulo_buscado = input("Título buscado: ").strip()
            titulo_buscado = tratar_acentos(titulo_buscado).lower()
            print("-" * 75)

        resultado = [] # Lista para armazenar filmes que correspondem à busca.

        for filme in catalogo:
            if titulo_buscado in tratar_acentos(filme[0]).lower(): # Verifica se o título buscado está contido em um dos títulos do catálogo (em minúsculas e sem acentos).
                resultado.append(filme)  # Adiciona o filme à lista de resultados se corresponder.
        
        if resultado: # Verifica se a lista de resultados contém filmes.
            print("Filme(s) correspondente(s):")
            print("-" * 75)
            cont = 1
            for filme in resultado: # Itera sobre a lista de resultados e imprime os detalhes de cada filme.
                print(f"Filme {cont}:")
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)
                cont += 1
            break # Encerra o loop de busca após exibir os resultados.

        else: # Se nenhum filme foi encontrado, capitaliza o título buscado para exibição.
            busca = titulo_buscado.capitalize()
            print(f"O filme de título '{busca}' não foi encontrado!")

        while True: # Loop para perguntar ao usuário se deseja buscar novamente.
            print("-" * 75)
            print("Deseja buscar o filme novamente?")
            print("s - Sim | n - Não")
            print("-" * 75)

            buscar_novamente = input("Sim ou Não? ").strip().lower() # Solicita ao usuário se deseja realizar outra busca.

            if buscar_novamente == 's':
                break # Se o usuário deseja buscar novamente, continua o loop de busca.
            elif buscar_novamente == 'n':
                print("Encerrando a busca...")
                return # Se o usuário não deseja buscar novamente, encerra a função.
            else: # Se a resposta for inválida, solicita uma nova resposta.
                print("Resposta inválida! Tente novamente:")
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                print("-" * 75)

def atualizar(): # Função para atualizar informações sobre filmes no catálogo.
    while True: # Loop que permitirá ao usuário fazer várias tentativas de atualizar filmes até que escolha sair.
        print("-" * 75)
        print("." * 3, "Qual filme você deseja atualizar?", "." * 3)
        print("-" * 75)

        atualizar_titulo = input("Título do filme a ser atualizado: ").strip().capitalize() # Solicita ao usuário o título do filme a ser atualizado.

        while not atualizar_titulo: # Verifica se o título fornecido não está vazio. Se estiver, pede ao usuário para fornecer um título válido.
            print("Título vazio!")
            print("Por favor, insira o título do filme que você deseja atualizar:")
            atualizar_titulo = input("Título a atualizar: ").strip().capitalize()

        filmes_para_atualizar = [] # Cria uma lista para armazenar os filmes que correspondem ao título fornecido.

        for filme in catalogo:
            if atualizar_titulo.lower() in tratar_acentos(filme[0]).lower(): # Verifica se o título buscado para a atualização está contido em um dos títulos do catálogo (em minúsculas e sem acentos).
                filmes_para_atualizar.append(filme) # Adiciona o filme à lista de filmes a serem atualizados se o título corresponder.
                print("-" * 75)
        
        if filmes_para_atualizar: # Se algum filme for encontrado, exibe as opções de atualização.
            print("Filme(s) correspondente(s):")
            print("-" * 75)
            cont = 1
            for filme in filmes_para_atualizar: # Mostra os filmes encontrados para o usuário.
                print(f"Filme {cont}:")
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)
                cont += 1
            
            print("Qual o número do filme que você deseja atualizar?")
            num_atualizar = input("Número: ").strip() # Solicita ao usuário o número do filme a ser atualizado.
            while not num_atualizar or not num_atualizar.isdigit() or not (1 <= int(num_atualizar) <= len(filmes_para_atualizar)): # Verifica se o número não está vazio, não for um número ou estiver fora do intervalo válido.
                if num_atualizar == "":
                    print("Número vazio!")
                    print("Insira, por favor:")
                elif not num_atualizar.isdigit():
                    print("Erro!")
                    print("O número do filme não pode ser um decimal,")
                    print("nem conter letras ou demais caracteres.")
                    print("Por favor, informe o número corretamente:")
                else:
                    print("Número inválido!")
                    if len(filmes_para_atualizar) == 1:
                        print("Por favor, digite um número 1.")
                        print("Há apenas 1 filme no catálogo.")
                    else:
                        print(f"Por favor, digite um número entre 1 e {len(filmes_para_atualizar)}")
                num_atualizar = input("Número: ").strip()

            filme_selecionado = filmes_para_atualizar[int(num_atualizar) - 1] # Seleciona o filme escolhido.

            while True: # Loop para permitir que o usuário escolha uma opção de atualização até que uma entrada válida seja fornecida.
                print("O que deseja atualizar?")
                print("1 - Título")
                print("2 - Diretor")
                print("3 - Ano")
                print("4 - Gênero")
                print("5 - Todos (Título, Diretor, Ano e Gênero)")
                print("-" * 75)

                opcao = input("Opção: ").strip() # Solicita ao usuário o que ele deseja atualizar.

                if opcao in ['1', '2', '3', '4', '5']: 
                    if opcao == '1': # Atualiza o título do filme verificando se ele não está vazio.
                        titulo_atualizado = input("Novo título: ").strip().capitalize() 
                        while not titulo_atualizado:
                            print("Título vazio!")
                            print("Por favor, insira o novo título:")
                            titulo_atualizado = input("Título: ").strip().capitalize()
                        filme_selecionado[0] = titulo_atualizado # Atualiza o título do filme selecionado com o novo título fornecido pelo usuário.
                        print(f"Título atualizado para '{titulo_atualizado}'.")
                    elif opcao == '2':  # Atualiza o diretor do filme, validando se não está vazio, se contém dígitos ou caracteres especiais.
                        diretor_atualizado = input("Novo diretor(a): ").strip().capitalize()
                        while not diretor_atualizado or diretor_atualizado.isdigit() or diretor_atualizado in '"!¹1/2²@?°3³#$4£5%¢6¨¬7&8*9()0-_=+§`´{}ª[]º^~<,>;:|\/*':
                            if diretor_atualizado == "":
                                print("Diretor(a) não informado!")
                                print("Informe para prosseguirmos:")
                            elif diretor_atualizado.isdigit():
                                print("Erro!")
                                print("O nome do diretor deve conter apenas letras")
                                print("e não dígitos numéricos.")
                                print("Informe corretamente, por favor:")
                            else:
                                print("Erro!")
                                print("O nome do diretor deve conter apenas letras")
                                print("e não os demais caracteres.")
                                print("Informe corretamente, por favor:")
                            diretor_atualizado = input("Novo diretor(a): ").strip().capitalize()
                        filme_selecionado[1] = diretor_atualizado # Atualiza o/a diretor(a) do filme selecionado com o/a novo(a) diretor(a) fornecido pelo usuário.
                        print(f"Diretor atualizado para '{diretor_atualizado}'.")
                    elif opcao == '3': # Atualiza o ano de lançamento do filme, validando o ano e verificando se ele está vazio ou não.
                        ano_lancamento_atualizado = input("Novo ano de lançamento: ").strip()
                        while not ano_lancamento_atualizado or not ano_lancamento_atualizado.isdigit() or not (1888 <= int(ano_lancamento_atualizado) <= 2024):
                            if ano_lancamento_atualizado == "":
                                print("Ano de lançamento vazio!")
                                print("Insira, por favor:")
                            elif not ano_lancamento_atualizado.isdigit():
                                print("Erro!")
                                print("O ano de lançamento não pode ser um decimal,")
                                print("nem conter letras ou demais caracteres.")
                                print("Por favor, informe o ano corretamente:")
                            else:
                                print("Ano inválido!")
                                print("Por favor, digite um ano entre 1888 e 2024")
                            ano_lancamento_atualizado = input("Novo ano de lançamento: ").strip()
                        filme_selecionado[2] = int(ano_lancamento_atualizado) # Atualiza o ano de lançamento do filme selecionado com o ano de lançamento fornecido pelo usuário.
                        print(f"Ano atualizado para '{ano_lancamento_atualizado}'.")
                    elif opcao == '4': # Atualiza o gênero do filme, verificando se ele está vazio ou se não é uma letra.
                        genero_atualizado = input("Novo gênero: ").strip().lower()
                        while not genero_atualizado or not genero_atualizado.isalpha():
                            if genero_atualizado == "":
                                print("O Gênero não foi informado.")
                                print("Insira, por favor:")
                            else:
                                print("O gênero deve conter apenas letras.")
                                print("Não deve apresentar dígitos numéricos ou demais caracteres.")
                                print("Por favor, informe o gênero do filme corretamente:")
                            genero_atualizado = input("Novo gênero: ").strip().lower()
                        filme_selecionado[3] = genero_atualizado # Atualiza o gênero do filme selecionado com o gênero fornecido pelo usuário.
                        print(f"Gênero atualizado para '{genero_atualizado}'.")
                    elif opcao == '5': # Atualiza todas as informações do filme.
                        novo_titulo = input("Novo título: ").strip().capitalize() # Atualiza o título do filme verificando se ele não está vazio.
                        while not novo_titulo:
                            print("Título vazio!")
                            print("Por favor, insira o novo título:")
                            novo_titulo = input("Novo título: ").strip().capitalize()
                        filme_selecionado[0] = novo_titulo # Atualiza o título do filme selecionado com o novo título fornecido pelo usuário.

                        novo_diretor = input("Novo(a) diretor(a): ").strip().capitalize() # Atualiza o diretor do filme, validando se não está vazio, se contém dígitos ou caracteres especiais.
                        while not novo_diretor or novo_diretor.isdigit() or novo_diretor in '"!¹1/2²@?°3³#$4£5%¢6¨¬7&8*9()0-_=+§`´{}ª[]º^~<,>;:|\/*':
                            if novo_diretor == "":
                                print("Diretor(a) não informado!")
                                print("Informe para prosseguirmos:")
                            elif novo_diretor.isdigit():
                                print("Erro!")
                                print("O nome do diretor deve conter apenas letras")
                                print("e não dígitos numéricos.")
                                print("Informe corretamente, por favor:")
                            else:
                                print("Erro!")
                                print("O nome do diretor deve conter apenas letras")
                                print("e não os demais caracteres.")
                                print("Informe corretamente, por favor:")
                            novo_diretor = input("Novo diretor(a): ").strip().capitalize()
                        filme_selecionado[1] = novo_diretor # Atualiza o/a diretor(a) do filme selecionado com o/a novo(a) diretor(a) fornecido pelo usuário.

                        novo_ano = input("Novo ano de lançamento: ").strip() # Atualiza o ano de lançamento do filme, validando o ano e verificando se ele está vazio ou não.
                        while not novo_ano or not novo_ano.isdigit() or not (1888 <= int(novo_ano) <= 2024):
                            if novo_ano == "":
                                print("Ano de lançamento vazio!")
                                print("Insira, por favor:")
                            elif not novo_ano.isdigit():
                                print("Erro!")
                                print("O ano de lançamento não pode ser um decimal,")
                                print("nem conter letras ou demais caracteres.")
                                print("Por favor, informe o ano corretamente:")
                            else:
                                print("Ano inválido!")
                                print("Por favor, digite um ano entre 1888 e 2024")
                            novo_ano = input("Novo ano de lançamento: ").strip()
                        filme_selecionado[2] = int(novo_ano) # Atualiza o ano de lançamento do filme selecionado com o ano de lançamento fornecido pelo usuário.

                        novo_genero = input("Novo gênero: ").strip().lower() # Atualiza o gênero do filme, verificando se ele está vazio ou se não é uma letra.
                        while not novo_genero or not novo_genero.isalpha():
                            if novo_genero == "":
                                print("O Gênero não foi informado.")
                                print("Insira, por favor:")
                            else:
                                print("O gênero deve conter apenas letras.")
                                print("Não deve apresentar dígitos numéricos ou demais caracteres.")
                                print("Por favor, informe o gênero do filme corretamente:")
                            novo_genero = input("Novo gênero: ").strip().lower()
                        filme_selecionado[3] = novo_genero # Atualiza o gênero do filme selecionado com o gênero fornecido pelo usuário.

                        print(f"Todos os dados do filme '{filme_selecionado[0]}' foram atualizados com sucesso!")

                    break # Encerra o loop de opções de atualização, pois a atualização foi concluída.
                else:
                    print("Opção inválida! Tente novamente.")

            return # Encerra a execução da função e volta ao fluxo principal do programa, onde a função foi originalmente chamada.

        else:
            print(f"O filme de título '{atualizar_titulo}' não foi encontrado!") # Se nenhum filme for encontrado, oferece a opção de buscar novamente.

            while True: # Loop para perguntar ao usuário se deseja buscar o filme novamente até que uma resposta válida seja fornecida.
                print("Deseja buscar o filme novamente?")
                print("s - Sim | n - Não")
                print("-" * 75)

                buscar_atualizar_novamente = input("Sim ou Não? ").strip().lower()  # Solicita ao usuário que informe se deseja buscar o filme novamente, removendo espaços em branco e convertendo para minúsculas.
                if buscar_atualizar_novamente == 's':
                    break # Se o usuário escolher 's', sai do loop e permite que o usuário tente buscar o filme novamente.
                elif buscar_atualizar_novamente == 'n':
                    print("Encerrando a atualização...")
                    return # Se o usuário escolher 'n', exibe uma mensagem de encerramento e encerra a função 'atualizar'.
                else:
                    print("Entrada inválida. Por favor, digite 's' para Sim ou 'n' para Não.")
                    print("-" * 75)

def remover(): # Função permite ao usuário remover um filme do catálogo com base no título fornecido.
    while True: # Loop para permitir que o usuário tente remover filmes várias vezes.
        print("-" * 75)
        print("." * 3, "Qual filme você deseja remover?", "." * 3)
        print("-" * 75)

        remover_titulo = input("Título do filme a ser removido: ").strip().capitalize()  # Solicita ao usuário o título do filme que deseja remover, capitalizando a primeira letra de cada palavra.

        while not remover_titulo: # Verifica se o título fornecido pelo usuário está vazio.
            print("Título vazio!")
            print("Por favor, insira o título do filme que você deseja remover:")
            remover_titulo = input("Título a remover: ").strip().capitalize()
        
        filmes_para_remover = [] # Cria uma lista vazia para armazenar filmes que correspondem ao título fornecido.

        for filme in catalogo:
            if remover_titulo.lower() in tratar_acentos(filme[0]).lower(): # Verifica se o título buscado para a remoção está contido em um dos títulos do catálogo (em minúsculas e sem acentos).
                filmes_para_remover.append(filme) # Adiciona o filme correspondente à lista de filmes para remover.

        if filmes_para_remover: # Verifica se há filmes na lista de filmes para remover.
            if len(filmes_para_remover) > 1: # Se houver mais de um filme correspondente, exibe a lista de filmes encontrados.
                print("Filme(s) correspondente(s):")
                print("-" * 75)
                cont = 1
                for filme in filmes_para_remover: # Mostra os filmes encontrados para o usuário.
                    print(f"Filme {cont}:")
                    print(f"- Título: {filme[0]}")
                    print(f"- Diretor(a): {filme[1]}")
                    print(f"- Ano de Lançamento: {filme[2]}")
                    print(f"- Gênero: {filme[3]}")
                    print("-" * 75)
                    cont += 1
                
                while True: # Loop para solicitar ao usuário o número do filme a ser removido até que uma entrada válida seja fornecida.
                    print("Qual o número do filme que você deseja remover?")
                    num_remover = input("Número: ").strip() # Recebe o número do filme a ser removido e remove espaços em branco.
                    if num_remover.isdigit():
                        num_remover = int(num_remover) # Converte a entrada para um número inteiro.
                        if 1 <= num_remover <= len(filmes_para_remover): # Verifica se o número está dentro do intervalo válido.
                            filme = filmes_para_remover[num_remover - 1] # Seleciona o filme correspondente ao número fornecido.
                            catalogo.remove(filme) # Remove o filme selecionado do catálogo.
                            print(f"O filme '{filme[0]}' foi removido com sucesso!")
                            break # Sai do loop de solicitação de número do filme.
                        else:
                            print(f"Número inválido! Por favor, digite um número entre '1' e '{len(filmes_para_remover)}'.")
                    elif num_remover == "":
                        print("Número vazio!")
                        print("Insira, por favor:")
                    else:
                        print("Erro!")
                        print("O número do filme não pode conter letras ou outros caracteres.")
                        print("Por favor, informe o número corretamente:")
            else: # Se houver apenas um filme correspondente, exibe as informações desse filme.
                print("-" * 75)
                print("Filme encontrado:")
                print(f"Filme 1:")
                filme = filmes_para_remover[0] # Seleciona o único filme encontrado.
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)

                while True: # Loop para solicitar ao usuário a confirmação para remover o único filme encontrado.
                    print("Qual o número do filme que você deseja remover?")
                    num_remover = input("Número: ").strip() # Recebe o número do filme a ser removido e remove espaços em branco.
                    if num_remover.isdigit():
                        num_remover = int(num_remover) # Converte a entrada para um número inteiro.
                        if num_remover == 1: # Verifica se o número fornecido é 1 (o único filme disponível).
                            catalogo.remove(filme) # Remove o filme do catálogo.
                            print(f"O filme '{filme[0]}' foi removido com sucesso!")
                            break # Sai do loop de solicitação de número do filme.
                        else: # Informa ao usuário que o número fornecido é inválido.
                            print(f"Número inválido.")
                            print("Há apenas um filme no catálogo. Digite '1' para remover o filme.")
                    elif num_remover == "": # Verifica se a entrada do usuário está vazia.
                        print("Número vazio!")
                        print("Insira, por favor:")
                    else: # Explica que o número deve ser um valor numérico.
                        print("Erro!")
                        print("O número do filme não pode conter letras ou outros caracteres.")
                        print("Por favor, informe o número corretamente.")
            
            break # Sai do loop após a remoção do filme.
        else: 
            print(f"O filme de título '{remover_titulo}' não foi encontrado!")
            
            while True: # Loop para perguntar ao usuário se deseja tentar buscar o filme novamente.
                print("Deseja buscar o filme novamente?")
                print("s - Sim | n - Não")
                print("-" * 75)

                buscar_remover_novamente = input("Sim ou Não? ").strip().lower() # Recebe a resposta do usuário, removendo espaços em branco e convertendo para minúsculas.
                if buscar_remover_novamente == 's': 
                    break # Se o usuário escolher 's', reinicia o loop para buscar o filme novamente.
                elif buscar_remover_novamente == 'n':
                    print("Encerrando a remoção...")
                    return # Se o usuário escolher 'n', encerra a função remover e retorna ao menu principal.
                else: # Se a entrada do usuário não for 's' ou 'n', informa que a entrada é inválida.
                    print("Entrada inválida. Por favor, digite 's' para Sim ou 'n' para Não.")
                    print("-" * 75)

menu()  # Chama a função 'menu'.
