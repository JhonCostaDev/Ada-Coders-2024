package app;

public class Telegram extends ServicoMensagem{
	@Override
	public void enviarMensagem(){
		//validarConexao();
		System.out.println("Telegram Enviando Mensagem ...");
		
	}
	@Override
	public void receberMensagem(){
		System.out.println("Recebendo Mensagem ...");
		//salvarHistoricoMensagem();
	}
}