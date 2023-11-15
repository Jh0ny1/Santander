# Override

Em Java, o método @Override é uma anotação que indica que um método em uma subclasse está destinado a substituir um método com a mesma assinatura na superclasse. Essa anotação é opcional, mas é uma prática recomendada para garantir que você está realmente sobrescrevendo um método e não criando inadvertidamente um novo método na subclasse.

Aqui estão alguns pontos importantes sobre o método @Override:

## 1. Assinatura do Método:

Para um método em uma subclasse ser considerado uma sobrescrita de um método na superclasse, ele deve ter a mesma assinatura. A assinatura inclui o nome do método, o tipo de retorno, e o tipo e a ordem dos parâmetros.


## 2. Exemplo de Uso:

Aqui está um exemplo de uma classe de superclasse (Pessoa) com um método (exibirDetalhes) e uma subclasse (Aluno) que sobrescreve esse método.

- Java

```java
public class Pessoa {
    public void exibirDetalhes() {
        System.out.println("Detalhes da Pessoa");
    }
}

public class Aluno extends Pessoa {
    @Override
    public void exibirDetalhes() {
        System.out.println("Detalhes do Aluno");
    }
}
```

## 3. Verificação em Tempo de Compilação:

Se você usar a anotação @Override e o método na subclasse não estiver realmente substituindo um método na superclasse, o compilador emitirá um erro. Isso ajuda a evitar erros comuns de digitação ou assinatura.

- Java

```java
@Override
public void exibirDetalhe() { // Erro de compilação: o método correto é exibirDetalhes
    System.out.println("Detalhes do Aluno");
}
```

## 4. Cenários de Sobrescrita:

A sobrescrita de métodos é comumente usada em situações em que uma subclasse precisa fornecer uma implementação específica para um método que já está definido na superclasse.

- Java

```java
public class Animal {
    public void fazerSom() {
        System.out.println("Som genérico de um animal");
    }
}

public class Cachorro extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("Latido de um cachorro");
    }
}
```

## 5. Chamando o Método da Superclasse:

Dentro de um método sobrescrito, você pode chamar o método correspondente da superclasse usando a palavra-chave super.

- Java

```java
public class Aluno extends Pessoa {
    @Override
    public void exibirDetalhes() {
        super.exibirDetalhes(); // Chama o método da superclasse
        System.out.println("Detalhes do Aluno");
    }
}
```

Isso é útil quando você deseja estender o comportamento existente do método na superclasse.

A anotação @Override é uma ferramenta valiosa para garantir a correção e a clareza do código ao trabalhar com hierarquias de classes em Java. Ela ajuda a evitar erros comuns e facilita a compreensão do código, indicando explicitamente que um método está substituindo outro na superclasse.