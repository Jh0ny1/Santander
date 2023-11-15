# Construtor

Em Java, um construtor é um bloco de código que é chamado quando uma instância de uma classe é criada. Ele tem o mesmo nome da classe e não possui um tipo de retorno. A principal finalidade de um construtor é inicializar os atributos (variáveis de instância) da classe e realizar qualquer outra configuração necessária durante a criação do objeto.

Aqui estão alguns pontos importantes sobre construtores em Java:

## 1. Nome do Construtor:

O construtor tem o mesmo nome da classe. Por exemplo, se a classe é chamada MinhaClasse, então o construtor seria MinhaClasse().


## 2. Múltiplos Construtores:

Uma classe pode ter vários construtores, desde que eles tenham parâmetros diferentes (conhecido como sobrecarga de construtores).


## 3. Chamada Implícita:

O construtor é chamado implicitamente quando um objeto da classe é criado usando a palavra-chave new.

Exemplo de uma classe com construtor:

- Java
```Java
public class MinhaClasse {
    // Atributos
    private int numero;

    // Construtor padrão (sem parâmetros)
    public MinhaClasse() {
        // Inicialização de atributos ou outras operações
        numero = 0;
    }

    // Construtor com parâmetros
    public MinhaClasse(int valor) {
        // Inicialização de atributos com valor fornecido
        numero = valor;
    }

    // Outros métodos da classe...
}
```

## 4. Construtor Padrão:

Se você não fornecer explicitamente um construtor para uma classe, o Java cria automaticamente um construtor padrão sem parâmetros.

- Java

```Java
public class Exemplo {
    // Construtor padrão é criado automaticamente se não houver construtor definido
}
```

Inicialização de Atributos:

Construtores são frequentemente usados para inicializar os atributos de uma classe com valores específicos quando um objeto é criado.


## 6. Herança:

Quando uma classe estende outra, o construtor da classe filha pode chamar o construtor da classe pai usando a palavra-chave super().

- Java

```Java
public class ClasseFilha extends ClassePai {
    public ClasseFilha() {
        super(); // Chamada ao construtor da classe pai
        // Restante do código do construtor da classe filha
    }
}
```


Os construtores são uma parte essencial da programação orientada a objetos em Java, pois fornecem um meio de inicializar objetos com valores específicos e realizar configurações necessárias durante a criação de instâncias de uma classe.