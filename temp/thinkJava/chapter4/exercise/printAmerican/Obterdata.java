import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Obterdata {
  public static void main(String[] args) {
    String timeStamp =
        new SimpleDateFormat("yyyy/MM/dd HH:mm:ss").format(Calendar.getInstance().getTime());

    System.out.println(timeStamp);
  }
}