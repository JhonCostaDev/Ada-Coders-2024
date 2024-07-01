public class Distance {
	public static void main(String [] args) {
	double dist = distance(1.9, 2.0, 4.0, 6.0);
	}

	public static double distance(double x1, double y1, double x2, double y2) {
		double dx = x2 - x1;
		double dy = y2 - y1;
		double dSquared = Math.sqrt(dx * dx + dy * dy);
		System.out.println("dx is: " + dx);
		System.out.println("dy is: " + dy);
		System.out.println("distance squared  is: " + dSquared);

		return 0.0;//stub
	}
}
