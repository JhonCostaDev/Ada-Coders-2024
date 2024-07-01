/*
Write a method called printAmerican that takes the day, date, month and year as parameters
and displays them in american format.
*/

public class PrintAmerican {
	public static void main(String [] args) {
		String date = "Segunda-feira, 01 de julho de 2024";

		printAmerican(date);
	}

	public static void printAmerican(String d) {
		String [] date = d.split(" ");
		String day = date[0];
		String aDate = date[1];
		String month = date[3];
		String year = date[5];

		System.out.printf("""
		%s %s %s %s
		""", day, month, aDate, year);

		/*
		for (String a : date) {
			System.out.println(a);
		} */
	}
}
