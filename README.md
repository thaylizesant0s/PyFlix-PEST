# PyFlix - Sistema de Gerenciamento de Filmes

PyFlix é um sistema de gerenciamento de filmes desenvolvido em Python. Ele permite adicionar, listar, buscar, atualizar e remover filmes de um catálogo. O objetivo do projeto é oferecer uma interface simples e eficiente para a gestão de uma coleção de filmes.

## Funcionalidades

- **Adicionar Filme**: Insere um novo filme no catálogo.
- **Listar Filmes**: Exibe todos os filmes cadastrados no catálogo.
- **Buscar Filmes**: Permite buscar filmes por parte do título.
- **Atualizar Filme**: Atualiza as informações de um filme já cadastrado.
- **Remover Filme**: Remove um filme do catálogo.

## Instruções de Execução

Maiúsculas e Minúsculas: O PyFlix não diferencia letras maiúsculas e minúsculas ao realizar buscas. Isso significa que, ao buscar um filme, você pode digitar tanto em letras maiúsculas quanto minúsculas, e o sistema encontrará os resultados adequados. Por exemplo, ao buscar por "Star Wars" ou "star wars", o sistema retornará o mesmo resultado.

Acentuação: A busca de filmes também leva em consideração a acentuação. Caso o título do filme tenha acentos, eles devem ser digitados corretamente para que o filme seja encontrado. Por exemplo, "Tropa de Elite" e "Tropa de Elite" serão tratados como o mesmo título, mas "Trope de Elite" não será reconhecido.

Tratamento de Erros: O sistema foi desenvolvido com mensagens claras para informar o usuário sobre possíveis entradas inválidas, como tentar remover ou atualizar um filme que não existe no catálogo, ou inserir uma opção de menu inválida. Se o catálogo estiver vazio ao realizar buscas, atualizações ou remoções, o sistema exibirá a mensagem "Catálogo vazio!".

Busca Parcial: Ao buscar filmes, você não precisa digitar o título completo. O sistema permite que você encontre filmes digitando apenas uma parte do título, facilitando a pesquisa.

## Decisões de Design Tomadas

Design do Menu

Simplicidade e Intuição: O menu apresenta opções numeradas de 1 a 6, facilitando a navegação pelos usuários.

Interação Direta: As opções são claramente definidas para cada funcionalidade (adicionar, listar, buscar, atualizar, remover filmes e sair).

Tratamento de Entradas Inválidas: Quando uma opção inválida é escolhida, o sistema exibe uma mensagem clara e retorna ao menu principal.

Acessibilidade: O design é acessível para usuários de todos os níveis, permitindo fácil compreensão e uso sem necessidade de conhecimento técnico avançado.
