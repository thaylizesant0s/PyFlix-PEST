catalogo = []

def menu():
    def inicio():
        print("-" * 75)
        print("." * 3, "Bem-vindo(a) à PyFlix!", "." * 3)
        print("-" * 75)

        while True:
            print("Deseja iniciar o programa?")
            print("s - Sim | n - Não")
            print("-" * 75)

            iniciar = input("Sim ou Não? ").strip().lower()

            if iniciar == 's':
                print("Carregando...")
                return True
            elif iniciar == 'n':
                print("Tudo bem...Tchau!")
                return False
            else:
                print("Resposta inválida! Tente novamente:")
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                print("-" * 75)

    def funcionalidades():
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

            opcao = input("Opção: ").strip()

            if opcao in ['1', '2', '3', '4', '5', '6']:
                return opcao
            else:
                print("Opção inválida! Tente novamente:")
    
    if inicio():
        while True:
            escolha = funcionalidades()
            if escolha == '1':
                adicionar()
            elif escolha == '6':
                print("Saindo...")
                break
            elif catalogo: 
                if escolha == '2':
                    listar()
                elif escolha == '3':
                    buscar()
                elif escolha == '4':
                    atualizar()
                elif escolha == '5':
                    remover()
            else:
                print("O catálogo está vazio!")
                print("Adicione algum filme antes de usar esta opção.")

def tratar_acentos(texto):
    acentuados = 'áàãâéêíóôõúüçÁÀÃÂÉÊÍÓÔÕÚÜÇ'
    sem_acento = 'aaaaeeiooouucAAAAEEIOOOUUC'
    
    texto_sem_acento = ""
    
    for caractere in texto:
        if caractere in acentuados:
            index = acentuados.index(caractere)
            texto_sem_acento += sem_acento[index]
        else:
            texto_sem_acento += caractere
    
    return texto_sem_acento

def adicionar():
    print("-" * 75)
    print("." * 3, "Informe as seguintes informações do filme que você deseja adicionar", "." * 3)
    print("-" * 75)

    titulo = input("Título: ").strip().capitalize()
    while not titulo:
        print("Título vazio!")
        print("Por favor, insira o título do filme:")
        titulo = input("Título: ").strip().capitalize()

    diretor_a = input("Diretor(a): ").strip().capitalize()
    while not diretor_a or diretor_a.isdigit() or diretor_a in '"!¹1/2²@?°3³#$4£5%¢6¨¬7&8*9()0-_=+§`´{}ª[]º^~<,>;:|\/*':
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

    ano_lancamento = input("Ano de lançamento: ").strip()
    while not ano_lancamento or not ano_lancamento.isdigit() or not (1888 <= int(ano_lancamento) <= 2024):
        if ano_lancamento == "":
            print("Ano de lançamento vazio!")
            print("Insira, por favor:")
        elif not ano_lancamento.isdigit():
            print("Erro!")
            print("O ano de lançamento não pode ser um decimal,")
            print("nem conter letras ou demias caracteres.")
            print("Por favor, informe o ano corretamente:")
        else:
            print("Ano inválido!")
            print("Por favor, digite um ano entre 1888 e 2024")
        ano_lancamento = input("Ano de lançamento: ").strip()

    genero = input("Gênero: ").strip().lower()
    while not genero or not genero.isalpha():
        if genero == "":
            print("O Gênero não foi informado.")
            print("Insira, por favor:")
        else:
            print("O gênero deve conter apenas letras.")
            print("Não deve apresentar dígitos numéricos ou demais caracteres.")
            print("Por favor, informe o gênero do filme corretamente:")
        genero = input("Gênero: ").strip().lower()

    print("-" * 75)

    novo_filme = [titulo, diretor_a, ano_lancamento, genero]
    catalogo.append(novo_filme)
    print(f"O filme '{titulo}' foi adicionado com sucesso!")

    print("-" * 75)

def listar():
    print("-" * 75)
    print("." * 2, "Seu catálogo de filmes:", "." * 2)
    print("-" * 75)

    cont = 1
    for filme in catalogo:
        print(f"Filme {cont}:")
        print(f"- Título: {filme[0]}")
        print(f"- Diretor(a): {filme[1]}")
        print(f"- Ano de Lançamento: {filme[2]}")
        print(f"- Gênero: {filme[3]}")
        print("-" * 75)
        cont += 1

def buscar():
    print("-" * 75)
    print("." * 2, "Por qual filme você busca?", "." * 2)
    print("-" * 75)

    while True:
        titulo_buscado = input("Título do filme buscado: ").strip()

        titulo_buscado = tratar_acentos(titulo_buscado).lower()
        print("-" * 75)

        while not titulo_buscado:
            print("Título vazio! Por favor, insira o título do filme que você deseja buscar:")
            titulo_buscado = input("Título buscado: ").strip()
            titulo_buscado = tratar_acentos(titulo_buscado).lower()
            print("-" * 75)

        resultado = []

        for filme in catalogo:
            if titulo_buscado in tratar_acentos(filme[0]).lower():
                resultado.append(filme)
        
        if resultado:
            print("Filme(s) correspondente(s):")
            print("-" * 75)
            cont = 1
            for filme in resultado:
                print(f"Filme {cont}:")
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)
                cont += 1
            break

        else:
            busca = titulo_buscado.capitalize()
            print(f"O filme de título '{busca}' não foi encontrado!")

        while True:
            print("-" * 75)
            print("Deseja buscar o filme novamente?")
            print("s - Sim | n - Não")
            print("-" * 75)

            buscar_novamente = input("Sim ou Não? ").strip().lower()

            if buscar_novamente == 's':
                break
            elif buscar_novamente == 'n':
                print("Encerrando a busca...")
                return 
            else:
                print("Resposta inválida! Tente novamente:")
                print("Por favor, digite 's' para Sim ou 'n' para Não.")
                print("-" * 75)

def atualizar():
    while True:
        print("-" * 75)
        print("." * 3, "Qual filme você deseja atualizar?", "." * 3)
        print("-" * 75)

        atualizar_titulo = input("Título do filme a ser atualizado: ").strip().capitalize()

        while not atualizar_titulo:
            print("Título vazio!")
            print("Por favor, insira o título do filme que você deseja atualizar:")
            atualizar_titulo = input("Título a atualizar: ").strip().capitalize()

        filmes_para_atualizar = []

        for filme in catalogo:
            if atualizar_titulo.lower() in tratar_acentos(filme[0]).lower():
                filmes_para_atualizar.append(filme)
                print("-" * 75)
        
        if filmes_para_atualizar:
            print("Filme(s) correspondente(s):")
            print("-" * 75)
            cont = 1
            for filme in filmes_para_atualizar:
                print(f"Filme {cont}:")
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)
                cont += 1
            
            print("Qual o número do filme que você deseja atualizar?")
            num_atualizar = input("Número: ").strip()
            while not num_atualizar or not num_atualizar.isdigit() or not (1 <= int(num_atualizar) <= len(filmes_para_atualizar)):
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

            filme_selecionado = filmes_para_atualizar[int(num_atualizar) - 1] 

            while True:
                print("O que deseja atualizar?")
                print("1 - Título")
                print("2 - Diretor")
                print("3 - Ano")
                print("4 - Gênero")
                print("5 - Todos (Título, Diretor, Ano e Gênero)")
                print("-" * 75)

                opcao = input("Opção: ").strip()

                if opcao in ['1', '2', '3', '4', '5']:
                    if opcao == '1':
                        titulo_atualizado = input("Novo título: ").strip().capitalize()
                        while not titulo_atualizado:
                            print("Título vazio!")
                            print("Por favor, insira o novo título:")
                            titulo_atualizado = input("Título: ").strip().capitalize()
                        filme_selecionado[0] = titulo_atualizado
                        print(f"Título atualizado para '{titulo_atualizado}'.")
                    elif opcao == '2':
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
                        filme_selecionado[1] = diretor_atualizado
                        print(f"Diretor atualizado para '{diretor_atualizado}'.")
                    elif opcao == '3':
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
                        filme_selecionado[2] = int(ano_lancamento_atualizado)
                        print(f"Ano atualizado para '{ano_lancamento_atualizado}'.")
                    elif opcao == '4':
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
                        filme_selecionado[3] = genero_atualizado
                        print(f"Gênero atualizado para '{genero_atualizado}'.")
                    elif opcao == '5':
                        novo_titulo = input("Novo título: ").strip().capitalize()
                        while not novo_titulo:
                            print("Título vazio!")
                            print("Por favor, insira o novo título:")
                            novo_titulo = input("Novo título: ").strip().capitalize()
                        filme_selecionado[0] = novo_titulo

                        novo_diretor = input("Novo(a) diretor(a): ").strip().capitalize()
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
                        filme_selecionado[1] = novo_diretor

                        novo_ano = input("Novo ano de lançamento: ").strip()
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
                        filme_selecionado[2] = int(novo_ano)

                        novo_genero = input("Novo gênero: ").strip().lower()
                        while not novo_genero or not novo_genero.isalpha():
                            if novo_genero == "":
                                print("O Gênero não foi informado.")
                                print("Insira, por favor:")
                            else:
                                print("O gênero deve conter apenas letras.")
                                print("Não deve apresentar dígitos numéricos ou demais caracteres.")
                                print("Por favor, informe o gênero do filme corretamente:")
                            novo_genero = input("Novo gênero: ").strip().lower()
                        filme_selecionado[3] = novo_genero

                        print(f"Todos os dados do filme '{filme_selecionado[0]}' foram atualizados com sucesso!")

                    break
                else:
                    print("Opção inválida! Tente novamente.")

            return

        else:
            print(f"O filme de título '{atualizar_titulo}' não foi encontrado!")

            while True:
                print("Deseja buscar o filme novamente?")
                print("s - Sim | n - Não")
                print("-" * 75)

                buscar_atualizar_novamente = input("Sim ou Não? ").strip().lower()
                if buscar_atualizar_novamente == 's':
                    break 
                elif buscar_atualizar_novamente == 'n':
                    print("Encerrando a atualização...")
                    return
                else:
                    print("Entrada inválida. Por favor, digite 's' para Sim ou 'n' para Não.")
                    print("-" * 75)

def remover():
    while True:
        print("-" * 75)
        print("." * 3, "Qual filme você deseja remover?", "." * 3)
        print("-" * 75)

        remover_titulo = input("Título do filme a ser removido: ").strip().capitalize()

        while not remover_titulo:
            print("Título vazio!")
            print("Por favor, insira o título do filme que você deseja remover:")
            remover_titulo = input("Título a remover: ").strip().capitalize()
        
        filmes_para_remover = []
        for filme in catalogo:
            if remover_titulo.lower() in tratar_acentos(filme[0]).lower():
                filmes_para_remover.append(filme)

        if filmes_para_remover:
            if len(filmes_para_remover) > 1:
                print("Filme(s) correspondente(s):")
                print("-" * 75)
                cont = 1
                for filme in filmes_para_remover:
                    print(f"Filme {cont}:")
                    print(f"- Título: {filme[0]}")
                    print(f"- Diretor(a): {filme[1]}")
                    print(f"- Ano de Lançamento: {filme[2]}")
                    print(f"- Gênero: {filme[3]}")
                    print("-" * 75)
                    cont += 1
                
                while True:
                    print("Qual o número do filme que você deseja remover?")
                    num_remover = input("Número: ").strip()
                    if num_remover.isdigit():
                        num_remover = int(num_remover)
                        if 1 <= num_remover <= len(filmes_para_remover):
                            filme = filmes_para_remover[num_remover - 1]
                            catalogo.remove(filme)
                            print(f"O filme '{filme[0]}' foi removido com sucesso!")
                            break
                        else:
                            print(f"Número inválido! Por favor, digite um número entre '1' e '{len(filmes_para_remover)}'.")
                    elif num_remover == "":
                        print("Número vazio!")
                        print("Insira, por favor:")
                    else:
                        print("Erro!")
                        print("O número do filme não pode conter letras ou outros caracteres.")
                        print("Por favor, informe o número corretamente:")
            else:
                print("-" * 75)
                print("Filme encontrado:")
                print(f"Filme 1:")
                filme = filmes_para_remover[0]
                print(f"- Título: {filme[0]}")
                print(f"- Diretor(a): {filme[1]}")
                print(f"- Ano de Lançamento: {filme[2]}")
                print(f"- Gênero: {filme[3]}")
                print("-" * 75)

                while True:
                    print("Qual o número do filme que você deseja remover?")
                    num_remover = input("Número: ").strip()
                    if num_remover.isdigit():
                        num_remover = int(num_remover)
                        if num_remover == 1:
                            catalogo.remove(filme)
                            print(f"O filme '{filme[0]}' foi removido com sucesso!")
                            break
                        else:
                            print(f"Número inválido.")
                            print("Há apenas um filme no catálogo. Digite '1' para remover o filme.")
                    elif num_remover == "":
                        print("Número vazio!")
                        print("Insira, por favor:")
                    else:
                        print("Erro!")
                        print("O número do filme não pode conter letras ou outros caracteres.")
                        print("Por favor, informe o número corretamente.")
            
            break
        else:
            print(f"O filme de título '{remover_titulo}' não foi encontrado!")
            
            while True:
                print("Deseja buscar o filme novamente?")
                print("s - Sim | n - Não")
                print("-" * 75)

                buscar_remover_novamente = input("Sim ou Não? ").strip().lower()
                if buscar_remover_novamente == 's':
                    break 
                elif buscar_remover_novamente == 'n':
                    print("Encerrando a remoção...")
                    return
                else:
                    print("Entrada inválida. Por favor, digite 's' para Sim ou 'n' para Não.")
                    print("-" * 75)

menu()
