package estabelecimento;
import equipamentos.copiadora.Copiadora;
import equipamentos.digitalizadora.Digitalizadora;
import equipamentos.impressora.Deskjet;
import equipamentos.impressora.Impressora;
import equipamentos.multifuncional.Multifuncional;

public class Loja {
	public static void main (String [] args) {
	/*Impressora impressora = new Deskjet();
	impressora.imprimir();*/

	Multifuncional mult = new Multifuncional();
	Impressora impressora = mult;
	Digitalizadora digitalizadora = mult;
	Copiadora copiadora = mult;

	impressora.imprimir();
	digitalizadora.digitalizar();
	copiadora.copiar();

	}
}
