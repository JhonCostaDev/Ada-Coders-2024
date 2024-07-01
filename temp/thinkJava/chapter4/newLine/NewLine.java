public class NewLine {
	public static void newLine(){
		System.out.println();
	}

	

	public static void main(String [] args) {
		System.out.println("First line ...");
		threeNewLine();
		System.out.println("Second line ...");
	}

	public static void threeNewLine(){
	newLine();
	newLine();
	newLine();
	}
}
