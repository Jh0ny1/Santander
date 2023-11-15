package JavaProgramaçãoOrientadaOjetos.Animais;

public class cachorro {

    public String nome;
    public String cor;
    public int altura;
    public double peso;
    public int tamanhoDoRabo;
    public String estadoDeEspirito;


    public void comer (){};
    public void latir (){
        System.out.println("au au au");
    }
    public String pegar(){
        return "Bolinha";

    } 
    public String interagir(String acao){

        switch (acao) {
            case "carinho": this.estadoDeEspirito = " feliz"; break;
            case "vai domir": this.estadoDeEspirito = " bravo"; break;
            case "dar comida": this.estadoDeEspirito = " com fome"; break;
            case "pisar na patinha": this.estadoDeEspirito = " triste"; break;
            
            default: this.estadoDeEspirito = " confuso"; break;
            
        }
    //    if (acao.equals("carinho")){
    //        this.estadoDeEspirito = "Feliz";
    //    }else if (acao.equals("vai dormir")) {
    //        this.estadoDeEspirito = "bravo";           
    //    }else{
    //        this.estadoDeEspirito = "neutro";
    //    }
    return estadoDeEspirito;
    }    
}
