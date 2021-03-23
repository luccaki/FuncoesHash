# Funções de Espalhamento pelos métodos de Divisão e Multiplicação
#### Arquivos
Esse projeto contém dois arquivos:
- `FunçõesDeEspalhamento.py` - Contém a biblioteca das funções Hash;
- `AED2_Projeto1.py` - Contém um código para testar a biblioteca acima.

------------

#### Implementação
- Para implementar essa biblioteca no seu código basta realizar o download do arquivo `FunçõesDeEspalhamento.py`, e mover ele para a pasta raiz do seu projeto.
- Depois disso, você deve implementar a bibliotecar utilizando o código `import FunçõesDeEspalhamento as FDE`, com apenas isso você consegue utilizar as funções `FDE.divisão()` e `FDE.multiplicacao()`

------------

#### Utilização
##### Função de espalhamento pelo método da divisão `FDE.divisão(M, K)`
`h(K) = K mod M`
Recebe dois valores K e M
- K - Uma lista de números naturais (chave/key)
- M - Um número natural (Recomendado um numero primo não próximo de uma potência de 2)

Essa função retorna uma lista ordenada com a seguinte sintaxe:
[X,[Y]], sendo X o valor de h(K) e Y uma lista dos valores K que tiveram colisão com h(K)

Exemplo: 
- `funcao = FDE.divisão(12, range(0,101))`, `funcao` irá receber a lista gerada pelos valores `M = 12` e `K = {0, 1, 2 ... 100}` na função Hash por divisão

##### Função de espalhamento pelo método da multiplicação `FDE.multiplicacao(M, K, A)`
`h(K) = M × ((K × A) mod 1)` *O maior inteiro que seja menor que h(K)*
Recebe três valores K, M e A
- K - Uma lista de números naturais (chave/key)
- M - Um número natural (Número de posições na tabela)
- A - Uma constante não negativa. 0 < A < 1.

Essa função retorna uma lista ordenada com a seguinte sintaxe:
[X,[Y]], sendo X o valor de h(K) e Y uma lista dos valores K que tiveram colisão com h(K)

Exemplo: 
- `funcao = FDE.multiplicacao(200, range(1,500001), 0.62)`, `funcao` irá receber a lista gerada pelos valores `M = 12`, `K = {1, 2, 3 ... 500000}` e `A = 0.62` na função Hash por multiplicação

------------

#### Como executar os testes
- Para executar e compilar esse projeto você precisa realizar o download da versão mais recente do python, pode realizar atraves deste link: https://www.python.org/downloads/;
- Depois de instalado, você pode abrir um prompt de comando ou um PowerShell na pasta raiz do projeto e executar o seguindo comando: `py AED2_Projeto1.py`;
- Com apenas isso você consegue executar os testes dessa biblioteca.

