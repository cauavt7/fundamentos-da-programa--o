# anotações de fundmentos da programação

## tipos de dados em python
1.string
2.numbr int
3.number float
4.boolean

## Operadores matematicos -basicos
+->adição
-->subtração
*->multiplicação
/->divisão

# operadores lógicios
and->e-> se dus condições forem verdadadeira< o resultado é verdadeiro.
or-> ou

## metodos em python
1 print()-> exibe informações no terminal.
2 input()-> captura informações do terminal.
3.lower() -> converte toda a string em minuscula.
4.upper() -> Converte toda a string em maiúscula.
isdigit -> Verifica se o valor contémnumero.

## Format em python
Estrutura condicionale
``if (se)`` ->  verifica se uma informação é (verdadeira). se for, ele executa o código.
``elif (senão se)``-> é usado pra testar varia condicoes ele so executa se todas as condicoes aneriores forem falsas
``else (senão)`` -> Executa o código se a condição if for false (falsa).

# laços de repeticão
é um recurso de programação que permite executar um conunto de comando varia vezes. tambem são chamados de loop, laços de repetição ou interação.
´´for´´- usamos quado sabemos quantas vezes quermos repetir algo.
sintax:
for variavelin range (inicio,fim):
   comandos
   [range()] -> metodoque aceita geração de numeros
   [inicio] -> ~é iinclusivo. é o primeiro numero a ser usado.
   [fim]-> é exclusivo. o número utilizado é o anterior a esse.
   ## escopo das Variaveis 
   escopo loca -> A variavel ela só é acessada dentro da estrutura que ela foi criada.
   escopo Globlal-> A variavel pode ser acessada por todo mundo.

   ## varições das variaveis
   variavel em memoria é decklarada quando você não pretende usar essa variavel em outros cenários.
   variavel contadora -> é utilizada para uma logica onde a repetição irá ser alterada.

int()-> A gente vai incluir qual variavel/dado mque queremos converter para número inteiro
float()->A gente vai incluir qual variavel/dado mque queremos converter para número decimal
str()->A gente vai incluir qual variavel/dado mque queremos converter para número para texto

## Boas praticas
1.Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cameelCase.
2.se voce observar alguma estrutura tiponome(), 90% de chance de ser uma função.
3. python não tem constante porem utulizamos o padrão case UPERCASE para simular que aquela variável não pode ser alterada.

'while' -> é utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
sintaxe:
whie condição:
     comandos

## funções em python
`definir` que uma função será declarada ;
`propriedade` -> Variavel em memória que irá receber um argumento.
`argumento` -> valor que ira prencher o espaço da propriedade

## estrutuera de dados
`list ou lista` -> Armazena valores e podem sr heterogenea ou homognea ou seja pode guardar valores de um mesmp tipo ou de diferentes tipos.
ex: list = []// lista vazia
list = ["willian",25,1.82]

`dict ou dicionario`-> Armazena CONJUNTOS DE VALORES (CHAVE : VALOR). As chaves e valores podem ser heterogeneas ou homogeneas.
1. Para obter ov alor de um conjunto em dict, você acessa pela chave.
Ex> ddos_usuario = {} // Dicionário Vazio
dados_usuario = {"nome" : "william", "cpf":111456985-98, "idade":25}
dados_usuario["nome"] => Devolve o valor, que é "William".

## POO
Em python,todo molde é declarado atraves de uma classe => [class].
Qualquer caracteristica dentro de uma classe, é chamada de [atributo] e são declaradas com variaveis.
as ações dentro de uma classe são chamadas de métodos e são declaradas como [funções].

4.[Self] -> Significa ele mesmo, o atributo de classe atual.
5.[constructor] -> é uma estrutura de como a classe será "copiada"

## cases em python
snake_case -> nome_aluno -> nome de variaveis,metodos(funções) e arquivos.
cammelcase -> nomeAluno -> nome de variaveis, métodos(funções). 'Mais atual'
pascalcase -> nomeAluno -> Classes.
kebab-case -> nome-aluno -> não utilizamos em python.

# precisamos criar um molde de uma pessoa => class
# carateristiicas -> atributos => variaveis
# ações -> métodos => funções