# Classes Abstratas

Em Java, uma classe abstrata é uma classe que não pode ser instanciada diretamente e frequentemente é usada como uma classe base para outras classes (subclasses). Ela pode conter métodos abstratos, que são métodos sem implementação que devem ser fornecidos pelas subclasses. Uma classe abstrata pode conter métodos concretos (com implementação) e atributos.


## 1. Declaração:

Para declarar uma classe como abstrata, utiliza-se a palavra-chave abstract antes da palavra-chave class.

- Java
```Java
public abstract class Animal {
    // Atributos e métodos podem ser incluídos
}
```

## 2. Métodos Abstratos:

Uma classe abstrata pode conter métodos abstratos, que são métodos sem implementação. Esses métodos são declarados com a palavra-chave abstract e não têm corpo.

- Java
```Java
public abstract class Animal {
    public abstract void fazerSom();
}
```

Subclasses que estendem uma classe abstrata devem fornecer implementações para todos os métodos abstratos.


## 3. Métodos Concretos:

Além dos métodos abstratos, uma classe abstrata pode conter métodos concretos com implementação.

- Java
```Java
public abstract class Animal {
    public abstract void fazerSom();

    public void dormir() {
        System.out.println("O animal está dormindo.");
    }
}
```

Subclasses podem herdar e usar esses métodos concretos ou podem optar por sobrescrevê-los.


## 4. Herança:

As classes abstratas são frequentemente usadas como classes base para herança. Uma classe abstrata pode ser estendida por uma ou mais subclasses.

- Java
```Java
public class Cachorro extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("Latido de um cachorro.");
    }
}
```

## 5. Instanciação e Construtores:

Como uma classe abstrata não pode ser instanciada diretamente, você não pode criar um objeto usando o operador new para uma classe abstrata.
No entanto, você pode ter construtores em uma classe abstrata, que são chamados quando uma subclasse é instanciada.


## 6. Múltipla Herança:

Uma classe abstrata em Java pode estender apenas uma única classe, mas pode implementar múltiplas interfaces. Isso ocorre porque o Java suporta apenas herança única de classes.

- Java
```Java
public abstract class Animal {
    // ...
}

public interface Nadador {
    void nadar();
}

public class Golfinho extends Animal implements Nadador {
    @Override
    public void fazerSom() {
        System.out.println("Som de um golfinho.");
    }

    @Override
    public void nadar() {
        System.out.println("O golfinho está nadando.");
    }
}

```

As classes abstratas são uma ferramenta poderosa na modelagem de hierarquias de classes em Java, permitindo encapsular comportamentos comuns e garantir que as subclasses forneçam implementações específicas necessárias. É importante notar que uma classe abstrata pode conter métodos com implementação, enquanto as interfaces não podem.