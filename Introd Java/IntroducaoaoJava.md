# **Introdução ao Java: Resumo Aprofundado**

### 1. **Setup:**
   - **Descrição:** Configuração inicial do ambiente Java para desenvolvimento.
   - **Detalhes:**
     - Instalação do JDK (Java Development Kit).
     - Configuração de variáveis de ambiente (JAVA_HOME, PATH).
     - Utilização de IDEs como Eclipse ou IntelliJ.

   **Termos Comuns:**
   - **JDK:** Java Development Kit, inclui o compilador e as ferramentas necessárias.
   - **JRE:** Java Runtime Environment, ambiente de execução para aplicativos Java.
   - **IDE:** Integrated Development Environment, ambiente integrado de desenvolvimento.
   - **Path:** Caminho do sistema usado para localizar executáveis Java.
   - **Compilação:** Processo de tradução de código-fonte Java para bytecode.
   - **Execução:** Executar o programa Java usando o JRE.

### 2. **Variáveis:**
   - **Descrição:** Conceitos fundamentais de variáveis em Java.
   - **Detalhes:**
     - Tipos de dados (int, double, char, boolean, etc.).
     - Declaração e inicialização de variáveis.
     - Escopo de variáveis.

   **Termos Comuns:**
   - **Declaração:** Informar o tipo e nome de uma variável.
   - **Inicialização:** Atribuir um valor inicial a uma variável.
   - **Tipo de Dados:** Classificação que especifica a natureza da informação.
   - **Escopo:** Região do código onde uma variável é válida.

### 3. **Operadores Booleanos | Tabela Verdade:**
   - **Descrição:** Manipulação de expressões booleanas em Java.
   - **Detalhes:**
     - Operadores lógicos (&&, ||, !).
     - Tabela Verdade.
     - Avaliação de expressões condicionais.

   **Termos Comuns:**
   - **&& (AND):** Retorna verdadeiro se ambas as condições forem verdadeiras.
   - **|| (OR):** Retorna verdadeiro se pelo menos uma condição for verdadeira.
   - **! (NOT):** Inverte o valor lógico da expressão.
   - **Tabela Verdade:** Tabela que mostra todas as combinações possíveis de valores booleanos.

### 4. **Estruturas Condicionais:**
   - **Descrição:** Tomada de decisões em Java.
   - **Detalhes:**
     - if, else if, else.
     - switch-case.
     - Operador ternário.

   **Termos Comuns:**
   - **Controle de Fluxo:** Direcionamento da execução do programa.
   - **Tomada de Decisão:** Estrutura que executa diferentes ações com base em condições.
   - **Bloco de Código:** Conjunto de instruções agrupadas.

### 5. **Manipulação de Strings e Datas:**
   - **Descrição:** Trabalho com strings e datas em Java.
   - **Detalhes:**
     - Métodos de String.
     - Classe `StringBuilder`.
     - Classe `Date` e `LocalDate`.

   **Termos Comuns:**
   - **Concatenação:** União de strings.
   - **Substring:** Parte de uma string.
   - **Parsing:** Conversão de uma string para outro tipo de dado.
   - **Formatação de Data:** Representação específica de informações temporais.

### 6. **Laços Numéricos:**
   - **Descrição:** Iteração sobre valores numéricos em Java.
   - **Detalhes:**
     - for loop.
     - while loop.
     - do-while loop.

   **Termos Comuns:**
   - **Iteração:** Repetição de um bloco de código.
   - **Incremento:** Aumento de um valor.
   - **Decremento:** Diminuição de um valor.
   - **Condição de Saída:** Critério para encerrar um loop.

### 7. **Vetores:**
   - **Descrição:** Trabalho com arrays em Java.
   - **Detalhes:**
     - Declaração e inicialização de arrays.
     - Acesso e modificação de elementos.
     - Arrays multidimensionais.

   **Termos Comuns:**
   - **Indexação:** Atribuição de um índice a um elemento.
   - **Elemento:** Valor armazenado em um array.
   - **Array Unidimensional:** Conjunto unidimensional de elementos.
   - **Array Multidimensional:** Matriz de elementos com múltiplas dimensões.

### 8. **Funções:**
   - **Descrição:** Definição e uso de funções em Java.
   - **Detalhes:**
     - Declaração de métodos.
     - Parâmetros e retorno de funções.
     - Recursividade.

   **Termos Comuns:**
   - **Método:** Bloco de código executável.
   - **Parâmetro:** Informação passada para um método.
   - **Retorno:** Valor enviado de volta por um método.
   - **Recursividade:** Chamar um método dentro de si mesmo.

### 9. **Comandos Básicos:**
   - **Descrição:** Comandos essenciais para manipulação de código em Java.
   - **Detalhes:**
     - `break` e `continue`.
     - `return`.
     - `System.out.println()`.

   **Termos Comuns:**
   - **Saída no Console:** Exibição de informações no console.
   - **Break:** Encerra um loop ou switch.
   - **Continue:** Pula para a próxima iteração de um loop.
   - **Return:** Retorna um valor de um método.

### **50 Comandos Básicos em Java:**
1. `public class NomeClasse { }`: Declaração básica de uma classe em Java.
2. `public static void main(String[] args) { }`: Ponto de entrada para o programa Java.
3. `// Comentário de uma linha`: Comentário para anotações no código.
4. `/* Comentário de múltiplas linhas */`: Comentário que abrange várias linhas.
5. `int idade = 25;`: Declaração e inicialização de uma variável inteira.
6. `double preco = 49.99;`: Declaração e inicialização de uma variável de ponto flutuante.
7. `char genero = 'M';`: Declaração e inicialização de uma variável caractere.
8. `boolean status = true;`: Declaração e inicialização de uma variável booleana.
9. `String nome = "John";`: Declaração e inicialização de uma variável do tipo String.
10. `if (idade > 18) { /* código */ }`: Estrutura condicional if para tomada de decisões.
11. `else { /* código */ }`: Bloco de código a ser executado se a condição do if for falsa.
12. `else if (idade < 18) { /* código */ }`: Bloco alternativo a ser avaliado se a primeira condição for falsa.
13. `switch (opcao) { case 1: /* código */ break; default: /* código */ }`: Estrutura switch-case para seleção múltipla.
14. `for (int i = 0; i < 10; i++) { /* código */ }`: Estrutura de repetição for.
15. `while (condicao) { /* código */ }`: Estrutura de repetição while.
16. `do { /* código */ } while (condicao);`: Estrutura de repetição do-while.
17. `break;`: Encerra a execução de um loop.
18. `continue;`: Pula para a próxima iteração de um loop.
19. `return valor;`: Retorna um valor de um método.
20. `System.out.println("Hello, World!");`: Imprime uma mensagem no console.
21. `Scanner scanner = new Scanner(System.in);`: Criação de um objeto Scanner para entrada de dados.
22. `int numero = scanner.nextInt();`: Leitura de um número do console usando Scanner.
23. `String input = scanner.nextLine();`: Leitura de uma linha de texto do console usando Scanner.
24. `System.out.print("Digite algo: ");`: Exibe uma mensagem no console sem quebra de linha.
25. `int resultado = (idade > 18) ? 1 : 0;`: Operador ternário para atribuição condicional.
26. `int soma = numero1 + numero2;`: Operação de adição.
27. `int diferenca = numero1 - numero2;`: Operação de subtração.
28. `int produto = numero1 * numero2;`: Operação de multiplicação.
29. `double quociente = (double) numero1 / numero2;`: Operação de divisão com tratamento de tipo.
30. `int resto = numero1 % numero2;`: Obtém o resto da divisão.
31. `numero++;`: Incrementa o valor da variável em 1.
32. `numero--;`: Decrementa o valor da variável em 1.
33. `int resultado = Math.abs(numero);`: Valor absoluto de um número.
34. `double potencia = Math.pow(base, expoente);`: Potenciação usando a classe Math.
35. `double raizQuadrada = Math.sqrt(numero);`: Raiz quadrada usando a classe Math.
36. `String sub = texto.substring(inicio, fim);`: Obtém uma subcadeia de caracteres de uma string.
37. `int length = texto.length();`: Obtém o comprimento de uma string.
38. `String maiusculas = texto.toUpperCase();`: Converte todos os caracteres de uma string para maiúsculas.
39. `String minusculas = texto.toLowerCase();`: Converte todos os caracteres de uma string para minúsculas.
40. `boolean igual = str1.equals(str2);`: Verifica se duas strings são iguais.
41. `boolean contem = str1.contains("substring");`: Verifica se uma string contém uma subcadeia específica.
42. `int index = str.indexOf("caractere");`: Obtém o índice da primeira ocorrência de uma substring.
43. `char caractere = str.charAt(0);`: Obtém o caractere na posição especificada de uma string.
44. `String[] array = new String[5];`: Declaração e inicialização de um array de strings.
45. `array[0] = "Elemento 1";`: Atribui um valor a um elemento específico de um array.
46. `int[] numeros = {1, 2, 3, 4, 5};`: Inicialização de um array com valores.
47. `int[][] matriz = new int[3][3];`: Declaração e inicialização de uma matriz.
48. `matriz[0][0] = 1;`: Atribui um valor a um elemento específico de uma matriz.
49. `void metodo() { /* código */ }`: Declaração de um método sem retorno.
50. `int dobro = calcularDobro(5);`: Chamada de um método com retorno.
