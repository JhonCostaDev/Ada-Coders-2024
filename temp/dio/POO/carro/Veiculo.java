public abstract class Veiculo {
	
	private String ligar = "Ligando";
	private String ligarFarol = "Ligando Farol";
	private String verificaCombustivel = "Verificando Combustivel";

	public void getLigar(){
		System.out.println(ligar);
	}

	public void getLigarFarol(){
		System.out.println(ligarFarol);
	}

	public void getVerificaCombustivel(){
		System.out.println(verificaCombustivel);
	}

	public abstract void mover();

}