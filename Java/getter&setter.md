# Getters e Setters

Getters e setters são métodos usados para acessar e modificar os valores dos atributos de uma classe em Java. Eles são uma parte importante do encapsulamento, um dos princípios fundamentais da programação orientada a objetos. Aqui está uma explicação mais detalhada sobre getters e setters:

## 1. Getter:

Um método getter é usado para obter (ou recuperar) o valor de um atributo privado de uma classe.

O nome do método começa com "get", seguido pelo nome do atributo com a primeira letra em maiúscula.

O método não recebe nenhum argumento e retorna o valor do atributo.

Exemplo:

- Java

```java
public class Exemplo {
    private int numero;

    // Getter para o atributo 'numero'
    public int getNumero() {
        return numero;
    }
}
```

Uso:

- Java

```java
Exemplo exemplo = new Exemplo();
int valor = exemplo.getNumero();
```


## 2. Setter:

Um método setter é usado para definir (ou modificar) o valor de um atributo privado de uma classe.

O nome do método começa com "set", seguido pelo nome do atributo com a primeira letra em maiúscula.

O método recebe um argumento que representa o novo valor do atributo e não retorna nenhum valor.

Exemplo:

- Java

```java
public class Exemplo {
    private int numero;

    // Setter para o atributo 'numero'
    public void setNumero(int novoNumero) {
        this.numero = novoNumero;
    }
}
```

Uso:

- Java

```java
Exemplo exemplo = new Exemplo();
exemplo.setNumero(42);
```

## 3. Benefícios de Getters e Setters:

Controle de Acesso: Getters e setters permitem controlar o acesso aos atributos de uma classe. Ao tornar os atributos privados e fornecer métodos para acessá-los, você pode controlar como esses valores são lidos e modificados.
Encapsulamento: Eles ajudam a encapsular a implementação interna de uma classe. Isso significa que você pode alterar a implementação interna (como a representação de dados) sem afetar o código que usa a classe, desde que os getters e setters permaneçam inalterados.


Exemplo de encapsulamento:

- Java

```java
public class Pessoa {
    private String nome;

    public String getNome() {
        return nome;
    }

    public void setNome(String novoNome) {
        if (novoNome != null && !novoNome.isEmpty()) {
            this.nome = novoNome;
        } else {
            System.out.println("Nome inválido.");
        }
    }
}
```

Ao usar um setter, você pode adicionar lógica de validação, como garantir que o novo valor do atributo seja válido antes de atribuí-lo. No exemplo acima, o nome só é definido se o novo nome não for nulo e não estiver vazio.