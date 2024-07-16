
import app.MSN;
import app.Facebook;
import app.Telegram;

public class Computador  {
	public static void main(String[] args) {
		MSN msn = new MSN();
		System.out.println("========MSN========");
		msn.enviarMensagem();
		msn.receberMensagem();
		
		Facebook face = new Facebook();
		System.out.println("========Facebook========");
		face.enviarMensagem();
		face.receberMensagem();

		Telegram tlg = new Telegram();
		System.out.println("========Telegram========");
		tlg.enviarMensagem();
		tlg.receberMensagem();

		
	}
}