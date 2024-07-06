package app;

public class MSN extends ServicoMensagem{
	
	@Override
	public void enviarMensagem(){
		//validarConexao();
		System.out.println("Msn Enviando Mensagem ...");
		
	}
	@Override
	public void receberMensagem(){
		System.out.println("Recebendo Mensagem ...");
		//salvarHistoricoMensagem();
	}

	
}