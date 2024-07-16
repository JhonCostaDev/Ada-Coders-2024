public class Main {
	public static void main(String[] args) {
		Carro fusca = new Carro();
		System.out.println("==========fusca==========");
		fusca.getVerificaCombustivel();
		fusca.getLigarFarol();
		fusca.getLigar();
		fusca.mover();

		System.out.println("==========Scania==========");
		Caminhao scania = new Caminhao();
		scania.getVerificaCombustivel();
		scania.getLigarFarol();
		scania.getLigar();
		scania.mover();	
	}
}