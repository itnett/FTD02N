import java.time.LocalDate;
     import java.time.LocalTime;

     public class DateTimeExample {
         public static void main(String[] args) {
             LocalDate date = LocalDate.now();
             LocalTime time = LocalTime.now();

             System.out.println("Current Date: " + date);
             System.out.println("Current Time: " + time);
         }
     }