// Definer en klasse
     public class Car {
         private String model;
         private int year;

         // Konstruktør
         public Car(String model, int year) {
             this.model = model;
             this.year = year;
         }

         // Metode
         public void displayDetails() {
             System.out.println("Model: " + model + ", Year: " + year);
         }
     }

     // Lag objekter av klassen
     public class Main {
         public static void main(String[] args) {
             Car car1 = new Car("Toyota", 2020);
             car1.displayDetails(); // Model: Toyota, Year: 2020
         }
     }