# PyFlix - Sistema de Gerenciamento de Filmes

PyFlix é um sistema de gerenciamento de filmes desenvolvido em Python. Ele permite adicionar, listar, buscar, atualizar e remover filmes de um catálogo. O objetivo do projeto é oferecer uma interface simples e eficiente para a gestão de uma coleção de filmes.

## Funcionalidades

- **Adicionar Filme**: Insere um novo filme no catálogo.
- **Listar Filmes**: Exibe todos os filmes cadastrados no catálogo.
- **Buscar Filmes**: Permite buscar filmes por parte do título.
- **Atualizar Filme**: Atualiza as informações de um filme já cadastrado.
- **Remover Filme**: Remove um filme do catálogo.

## Instruções de Execução

## **Interatividade do PyFlix**

- **Maiúsculas e Minúsculas**: 
  - O PyFlix não diferencia letras maiúsculas e minúsculas ao realizar buscas. 
  - Isso significa que, ao buscar um filme, você pode digitar tanto em letras maiúsculas quanto minúsculas, e o sistema encontrará os resultados adequados.
  - Por exemplo, ao buscar por **"Star Wars"** ou **"star wars"**, o sistema retornará o mesmo resultado.

- **Acentuação**: 
  - A busca de filmes também leva em consideração a acentuação. 
  - Caso o título do filme tenha acentos, eles devem ser digitados corretamente para que o filme seja encontrado.
  - Por exemplo, **"Tropa de Elite"** e **"Tropa de Elite"** serão tratados como o mesmo título, mas **"Trope de Elite"** não será reconhecido.

- **Tratamento de Erros**: 
  - O sistema foi desenvolvido com mensagens claras para informar o usuário sobre possíveis entradas inválidas, como:
    - Tentar remover ou atualizar um filme que não existe no catálogo.
    - Inserir uma opção de menu inválida.
  - Se o catálogo estiver vazio ao realizar buscas, atualizações ou remoções, o sistema exibirá a mensagem **"Catálogo vazio!"**.

- **Busca Parcial**: 
  - Ao buscar filmes, você não precisa digitar o título completo.
  - O sistema permite que você encontre filmes digitando apenas uma parte do título, facilitando a pesquisa.

## Decisões de Design Tomadas

 **Design do Menu**

- **Simplicidade e Intuição**: 
  - O menu é estruturado de forma a apresentar opções numeradas de **1 a 6**, permitindo uma navegação rápida e intuitiva. 
  - Isso ajuda os usuários a entenderem imediatamente quais opções estão disponíveis.

- **Interação Direta**: 
- Cada opção do menu é claramente definida para corresponder a uma funcionalidade específica:
    - **1**: Adicionar Filme
    - **2**: Listar Filmes
    - **3**: Buscar Filmes
    - **4**: Atualizar Filme
    - **5**: Remover Filme
    - **6**: Sair
  - Essa abordagem elimina confusões e permite que os usuários selecionem rapidamente a ação desejada.

- **Tratamento de Entradas Inválidas**: 
  - O sistema é projetado para lidar com entradas inválidas de maneira eficaz, exibindo mensagens claras e informativas.
  - Quando uma opção fora do intervalo é escolhida, o menu retorna automaticamente ao estado original, evitando travamentos e mantendo a fluidez da interação.

- **Acessibilidade**: 
  - O design é amigável e acessível a usuários de todos os níveis de experiência, desde novatos até usuários mais avançados.
  - Não é necessário ter um conhecimento técnico prévio, pois as instruções são simples e diretas, facilitando a navegação e o uso do sistema.

- **Consistência Visual**:
  - O menu mantém uma estética visual consistente, com espaçamento adequado e formatação clara, o que contribui para uma experiência de usuário agradável.
  - O uso de texto em caixa alta e numeração facilita a leitura e a seleção de opções.



