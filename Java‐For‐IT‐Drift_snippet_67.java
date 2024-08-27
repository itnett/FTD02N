@ShellComponent
   public class MyCommands {

       @ShellMethod("Sier hei til brukeren")
       public String hei(String navn) {
           return "Hei " + navn;
       }
   }