package app;

public class Facebook extends ServicoMensagem {
	@Override
	public void enviarMensagem(){
		//validarConexao();
		System.out.println("Facebook Enviando Mensagem ...");
		
	}
	@Override
	public void receberMensagem(){
		System.out.println("Recebendo Mensagem ...");
		//salvarHistoricoMensagem();
	}
}