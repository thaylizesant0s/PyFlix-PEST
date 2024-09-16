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

Estrutura do Código
O sistema foi projetado de forma modular, com cada função correspondendo a uma operação específica (adicionar, listar, buscar, atualizar, remover filmes), facilitando a manutenção e a futura adição de novas funcionalidades.

Design do Menu
O menu principal do PyFlix foi desenvolvido com uma abordagem simples e clara para garantir uma experiência de usuário intuitiva e acessível. As opções são numeradas de 1 a 6, e cada número corresponde a uma ação específica (adicionar, listar, buscar, atualizar, remover filmes ou sair do programa).

Interatividade e Facilidade de Navegação
Simplicidade: O design minimalista do menu é intencional. Ele foi pensado para usuários que podem não ter familiaridade com interfaces de texto, facilitando a interação sem sobrecarregar o usuário com informações desnecessárias.
Clareza nas Opções: Cada opção do menu é descrita de forma direta, como "Adicionar Filme" ou "Buscar Filme", o que ajuda o usuário a saber exatamente o que cada ação fará sem ambiguidade.
Prevenção de Erros: O sistema trata entradas incorretas, como a escolha de um número fora das opções disponíveis, exibindo a mensagem "Opção inválida! Tente novamente". Esse feedback imediato evita que o usuário fique confuso e permite uma correção rápida, sem interromper a experiência.
Acessibilidade: Ao usar apenas números para seleção, o menu é acessível a uma ampla variedade de usuários, independentemente de sua experiência com sistemas interativos. Isso também permite uma navegação rápida e direta, sem complicações.
Interface do Usuário
A interface é totalmente baseada em texto, proporcionando um ambiente familiar para quem usa terminais de comando, como desenvolvedores ou estudantes. Ao manter o foco em texto puro, o PyFlix consegue ser leve e eficiente, rodando em praticamente qualquer ambiente com suporte a Python.
