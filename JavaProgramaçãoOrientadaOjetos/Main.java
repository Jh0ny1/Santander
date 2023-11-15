package JavaProgramaçãoOrientadaOjetos;

import JavaProgramaçãoOrientadaOjetos.Animais.cachorro;

public class Main {
    
public static void main(String[] args) {



cachorro cachorro01 = new cachorro();

cachorro01.nome = "Puppy";
cachorro01.cor = "Marron";
cachorro01.altura = 25;
cachorro01.peso = 5.5;
cachorro01.tamanhoDoRabo = 4;

cachorro01.latir();
cachorro01.comer();
System.out.println("O cachorro trouxe uma " + cachorro01.pegar());


System.out.println("O cachorro " + cachorro01.nome + " esta " + cachorro01.interagir("carinho"));
System.out.println("O cachorro " + cachorro01.nome + " esta " + cachorro01.interagir("vai domir"));
System.out.println("O cachorro " + cachorro01.nome + " esta " + cachorro01.interagir("pisar na patinha"));
System.out.println("O cachorro " + cachorro01.nome + " esta " + cachorro01.interagir("dar comida"));
System.out.println("O cachorro " + cachorro01.nome + " esta " + cachorro01.interagir("batata"));
}















}
