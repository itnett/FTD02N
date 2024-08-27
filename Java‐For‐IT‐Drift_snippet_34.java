@ShellComponent
public class MyCommands {
    
    @ShellMethod("Sier hei til brukeren")
    public String hei(String navn) {
        return "Hei " + navn;
    }

    @ShellMethod("Legger til to tall")
    public int leggTil(int a, int b) {
        return a + b;
    }
}