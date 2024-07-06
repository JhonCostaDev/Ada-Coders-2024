package app;

public abstract class ServicoMensagem {
	private void validarConexao(){
		System.out.println("Validando Conexao ...");
	}

	public abstract void enviarMensagem();
	
	public abstract void receberMensagem();
	
	private void salvarHistoricoMensagem(){
		System.out.println("Salvando Historico ...");
	}
}