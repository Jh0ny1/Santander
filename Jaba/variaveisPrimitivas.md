# Variaveis primitivas

Em Java, as variáveis primitivas são tipos de dados básicos que armazenam valores simples. Elas não são objetos e ocupam uma quantidade fixa de espaço na memória. Aqui estão os tipos de variáveis primitivas em Java:

## Inteiros:

+ byte: 8 bits, intervalo de -128 a 127.

+ short: 16 bits, intervalo de -32,768 a 32,767.

+ int: 32 bits, intervalo de -2^31 a 2^31-1.

+ long: 64 bits, intervalo de -2^63 a 2^63-1.


Exemplo:

- Java

```java
int idade = 25;
long populacaoMundial = 7800000000L; // L no final indica que é do tipo long
```

Ponto Flutuante:
+ float: 32 bits, precisão de ponto flutuante simples.
+ double: 64 bits, precisão de ponto flutuante duplo.


Exemplo:
- Java

```java
float altura = 1.75f; // f no final indica que é do tipo float
double preco = 99.99;
```

Caracteres:
+ char: 16 bits, representa um caractere Unicode.


Exemplo:

- Java

```java
char letra = 'A';
```

Booleano:
+ boolean: Representa um valor verdadeiro ou falso.


Exemplo:
- Java

```java
boolean estaChovendo = false;
```

Essas variáveis primitivas são utilizadas para armazenar valores simples e são fundamentais na programação Java. Elas têm diferentes tamanhos de armazenamento e são escolhidas com base nos requisitos específicos do programa.