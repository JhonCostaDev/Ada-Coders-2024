package equipamentos.multifuncional;

import equipamentos.copiadora.Copiadora;

import equipamentos.digitalizadora.Digitalizadora;

import equipamentos.impressora.Impressora;

public class Multifuncional implements Copiadora, Digitalizadora, Impressora {
	public void copiar() {
		System.out.println("Copiando de Multifuncional...");
	}

	public void digitalizar() {
			System.out.println("Digitalizando de Multifuncional...");
	}

	public void imprimir() {
			System.out.println("Imprimindo de Multifuncional...");
	}

} 
