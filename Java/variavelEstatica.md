# Variavel Estatica

Uma variável estática em Java é uma variável que pertence à classe, em vez de pertencer a instâncias individuais da classe. Isso significa que há apenas uma cópia da variável estática, independentemente de quantas instâncias da classe são criadas. As variáveis estáticas são declaradas com a palavra-chave static e são compartilhadas entre todas as instâncias da classe.

Aqui estão alguns pontos importantes sobre variáveis estáticas em Java:

## 1. Declaração de Variável Estática:

A sintaxe para declarar uma variável estática é adicionar a palavra-chave static à declaração da variável.

Exemplo:
- Java

```java
public class Exemplo {
    // Variável estática
    static int contador;

    // Outros membros da classe...
}
```

## 2. Acesso à Variável Estática:

Variáveis estáticas podem ser acessadas usando o nome da classe, seguido por ponto e o nome da variável.

Exemplo:
- Java

```java
// Acesso à variável estática
int valor = Exemplo.contador;
```

## 3. Inicialização de Variável Estática:

Variáveis estáticas são inicializadas quando a classe é carregada pela primeira vez. Isso ocorre antes da criação de qualquer instância da classe.

Exemplo:
- Java

```java
public class Exemplo {
    // Variável estática inicializada
    static int contador = 0;

    // Outros membros da classe...
}
```

## 4. Método Estático:

Muitas vezes, variáveis estáticas são usadas em conjunto com métodos estáticos. Métodos estáticos também pertencem à classe e não a instâncias específicas.

Exemplo:
- Java

```java
public class Exemplo {
    // Variável estática
    static int contador;

    // Método estático que usa a variável estática
    static void incrementarContador() {
        contador++;
    }
}
```

Uso:

- Java

```java
// Chama o método estático
Exemplo.incrementarContador();
```

## 5. Uso Comum:

Variáveis estáticas são frequentemente usadas para representar dados que são compartilhados por todas as instâncias da classe, como contadores, configurações globais, ou constantes.

Exemplo:

- Java

```java
public class Configuracao {
    // Variável estática para armazenar uma configuração global
    public static String idiomaPadrao = "Inglês";
}
```

## 6. Atenção ao Compartilhamento de Estado:

Embora variáveis estáticas forneçam um meio de compartilhar estado entre instâncias da classe, é importante usá-las com cuidado, pois o compartilhamento excessivo de estado pode levar a problemas de concorrência e dificultar o rastreamento do fluxo de dados.


Em resumo, variáveis estáticas em Java oferecem uma maneira de compartilhar informações entre instâncias de uma classe e são frequentemente usadas para representar dados globais ou constantes associadas à classe.