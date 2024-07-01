public class PrintTime {
	public static void main(String[] args) {
		int hour = 10;
		int minute = 53;

		printTime(hour, minute);
	}

	public static void printTime(int hour, int minute) {
		/*System.out.println(hour);
		System.out.println(":");
		;
		*/
		System.out.printf("""
		Time: %d : %d
		
		""", hour, minute);
	}
}
