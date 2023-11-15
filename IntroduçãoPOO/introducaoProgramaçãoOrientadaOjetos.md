# Introdução à Programação Orientada a Objetos em Java

A Programação Orientada a Objetos (POO) é um paradigma fundamental em Java, baseando-se em conceitos-chave, como classes, objetos, métodos, encapsulamento, herança, e polimorfismo, para criar código modular e reutilizável.

### 1. Hello, World! com Java

**Resumo:** A tradição de começar com um "Hello, World!" em Java envolve criar uma classe básica, normalmente chamada de `Main`, que contém o método `main`, o ponto de entrada para o programa Java.

**Termos Comuns:**
- java

``` Java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 2. Classes Não Executáveis

Resumo: Classes não executáveis servem como modelos para objetos. Elas encapsulam atributos e métodos que podem ser utilizados por outras classes.

Termos Comuns:

- Java
```java

public class Carro {
    String modelo;
    int ano;
    void acelerar() {
        // lógica de aceleração
    }
}
```
   ### 3. Métodos

Resumo: Métodos são blocos de código que realizam tarefas específicas. A assinatura do método define seu nome, tipo de retorno, e parâmetros.

Termos Comuns:

- Java

```Java

public class Calculadora {
    int somar(int a, int b) {
        return a + b;
    }
}
```

   ### 4. Encapsulamento

Resumo: Encapsulamento oculta detalhes internos de uma classe, permitindo controle sobre quem pode acessar seus membros. Modificadores de acesso como private são cruciais.

Termos Comuns:

- Java
```Java
public class Pessoa {
    private String nome;

    public String getNome() {
        return nome;
    }

    public void setNome(String novoNome) {
        this.nome = novoNome;
    }
}
``` 
    
 ### 5. Modelagem Orientada a Objetos

Resumo: Modelagem orientada a objetos representa entidades do mundo real como objetos interagindo entre si. Herança permite a criação de hierarquias de classes.

Termos Comuns:

- Java
```Java
public class Animal {
    // atributos e métodos comuns
}

public class Cachorro extends Animal {
    // atributos e métodos específicos de Cachorro
}
```    
    
   ### 6. Herança

Resumo: Herança permite que uma classe herde atributos e métodos de outra, promovendo reutilização de código. Classes pai (superclasse) e filho (subclasse) são conceitos essenciais.

Termos Comuns:

- Java
```Java
public class Animal {
    // atributos e métodos
}

public class Mamifero extends Animal {
    // atributos e métodos específicos de mamíferos
}
 ```   
    
### 7. Polimorfismo

Resumo: Polimorfismo permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum. Isso é alcançado através de métodos com a mesma assinatura.

Termos Comuns:

- Java
```Java
public interface Animal {
    void fazerSom();
}

public class Cachorro implements Animal {
    public void fazerSom() {
        System.out.println("Latindo...");
    }
}
```

   ### 8. Para Virar Mestre

Resumo: Tornar-se mestre requer prática constante. Interfaces e classes abstratas são avanços importantes. O entendimento profundo desses conceitos se desenvolve através da aplicação prática.

Termos Comuns:

- Java
```Java
public interface Autenticavel {
    boolean autenticar(String senha);
}

public abstract class ContaBancaria {
    // métodos comuns a todas as contas bancárias
    abstract void calcularTaxa();
}
```


Este resumo aprofundado fornece não apenas definições, mas também exemplos práticos para consolidar a compreensão dos conceitos essenciais da Programação Orientada a Objetos em Java. A prática ativa com esses conceitos em projetos reais é fundamental para a maestria.


